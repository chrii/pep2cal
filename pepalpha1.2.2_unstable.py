import datetime
tupwoche = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")
class Dcut():
    def __init__(self):
        self.wochentag = {}
        
    def daycutter(self, day):
        self.day = day
        pepsplit = self.day.strip().split(" ")
        pepcut = [x for x in pepsplit if x != '']
        if pepcut[-1] == "note:":
            del pepcut[-1]
        del pepcut[2]
        pepcut[0] = pepcut[0][:-1]
        return pepcut

    def add_list(self, tag_h):        
        self.wochentag[tag_h] = []

    def add_entry(self, tag_h, s_time):
        self.wochentag[tag_h].append(s_time)

class dateprint():
    def dater(self, dat, ctag, g):
        print("Dienst"+","+g+","+dat(int(ctag[0][1][:-3]), str(ctag[0][1][2:]))+","+dat(int(ctag[0][3][:-3]), str(ctag[0][3][2:]))+"\n")

"""
class datewrite():
    print("Der PEP-Eintrag wurde geschrieben")
    def dater(self, dat, ctag, g):
        file.write("Dienst"+","+g+","+dat(int(ctag[0][1][:-3]), str(ctag[0][1][2:]))+","+dat(int(ctag[0][3][:-3]), str(ctag[0][3][2:]))+"\n")
"""
def kwoche(year, kw):
    fourth_of_january = datetime.date(year,1,4).weekday()
    first_monday = datetime.date(year,1,4-fourth_of_january)
    monday_of_kw = first_monday + datetime.timedelta(days=(kw-1)*7)
    data = []
    for i in range(7):
        d = monday_of_kw + datetime.timedelta(days=i)
        data.append("%s.%s" % (d.day, d.month))
    return data

def wformat(v):
    kw_format = kwoche(yearin,kwin)[v].split(".")
    if len(kw_format[0]) < 2 and len(kw_format[1]) < 2:
        kw_format_new = "0"+kw_format[1]+"/"+"0"+kw_format[0]+"/"+str(yearin)
        return kw_format_new
    elif len(kw_format[0]) < 2:
        kw_format_new = kw_format[1]+"/"+"0"+kw_format[0]+"/"+str(yearin)
        return kw_format_new
    elif len(kw_format[1]) < 2:
        kw_format_new = "0"+kw_format[1]+"/"+kw_format[0]+"/"+str(yearin)
        return kw_format_new
    else:
        kw_format_new = kw_format[1]+"/"+kw_format[0]+"/"+str(yearin)
        return kw_format_new
    
yearin = 2018
kwin = 6
dcut = Dcut()
count = 0
with open("pepweek.txt", "r") as file:
    for line in file:

        d_cut = dcut.daycutter(line)
        dcut.add_list(d_cut[0])
        dcut.add_entry(d_cut[0], d_cut[1])
        dcut.add_entry(d_cut[0], d_cut[2])
        dcut.add_entry(d_cut[0], wformat(count))
        if count <= 5:
            count = count + 1

print(dcut.wochentag)