import datetime
yearin = int(input("Gib das Jahr an: "))
if len(str(yearin)) != 4:
    print("Keine gültige Jahreszahl")
kwin = int(input("Gib die Kalenderwoche an: "))
wochentag = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag")
Montag = []
Dienstag = []
Mittwoch = []
Donnerstag = []
Freitag = []
Samstag = []
Sonntag = []

def daycutter(day):
    pepsplit = day.strip().split(" ")
    pepcut = [x for x in pepsplit if x != '']
    if pepcut[-1] == "note:":
        del pepcut[-1]

    if "Montag" in pepcut[0][:-1]:
        Montag.append(pepcut)
    elif "Dienstag" in pepcut[0][:-1]:
        Dienstag.append(pepcut)
    elif "Mittwoch" in pepcut[0][:-1]:
        Mittwoch.append(pepcut)
    elif "Donnerstag" in pepcut[0][:-1]:
        Donnerstag.append(pepcut)
    elif "Freitag" in pepcut[0][:-1]:
        Freitag.append(pepcut)
    elif "Samstag" in pepcut[0][:-1]:
        Samstag.append(pepcut)
    elif "Sonntag" in pepcut[0][:-1]:
        Sonntag.append(pepcut)
with open("pepweek.txt", "r") as file:
##    pep = []
    for line in file:
        daycutter(line)


def kalenderwoche(year, kw):
    fourth_of_january = datetime.date(year,1,4).weekday()
    first_monday = datetime.date(year,1,4-fourth_of_january)
    monday_of_kw = first_monday + datetime.timedelta(days=(kw-1)*7)
    data = []
    for i in range(7):
        d = monday_of_kw + datetime.timedelta(days=i)
        data.append("%s.%s" % (d.day, d.month))
    return data

#dummy = 2018
#print(kalenderwoche(yearin,kwin)[0].split("."))

def wkek(wo_tag, s):
        if "Montag" == wo_tag:
            if "FREI" != Montag[0][3]:
                file.write("Dienst"+","+s+","+Montag[0][1]+","+Montag[0][3]+"\n")
        elif "Dienstag" == wo_tag:
            if "FREI" != Dienstag[0][3]:
                file.write("Dienst"+","+s+","+Dienstag[0][1]+","+Dienstag[0][3]+"\n")
        elif "Mittwoch" == wo_tag:
            if "FREI" != Mittwoch[0][3]:
                file.write("Dienst"+","+s+","+Mittwoch[0][1]+","+Mittwoch[0][3]+"\n")
        elif "Donnerstag" == wo_tag:
            if "FREI" != Donnerstag[0][3]:
                file.write("Dienst"+","+s+","+Donnerstag[0][1]+","+Donnerstag[0][3]+"\n")
        elif "Freitag" == wo_tag:
            if "FREI" != Freitag[0][3]:
                file.write("Dienst"+","+s+","+Freitag[0][1]+","+Freitag[0][3]+"\n")
        elif "Samstag" == wo_tag:
            if "FREI" != Samstag[0][3]:
                file.write("Dienst"+","+s+","+Samstag[0][1]+","+Samstag[0][3]+"\n") 
        elif "Sonntag" == wo_tag:
            if "FREI" != Sonntag[0][3]:
                file.write("Dienst"+","+s+","+Sonntag[0][1]+","+Sonntag[0][3]+"\n")
def formatierung(kek, v):
    kw_format = kalenderwoche(yearin,kwin)[v].split(".")
    if len(kw_format[0]) == 1:
        kw_format_new = "0"+kw_format[1]+"/"+"0"+kw_format[0]+"/"+str(yearin)
        wkek(y, kw_format_new)
    elif len(kw_format[1]) == 1:
        kw_format_new = "0"+kw_format[1]+"/"+kw_format[0]+"/"+str(yearin)
        wkek(y, kw_format_new)
    else:
        kw_format_new = kw_format[1]+"/"+kw_format[0]+"/"+str(yearin)
        wkek(y, kw_format_new)
        #wkek(y)
file = open("schreiben.csv", "w")
file.write("Subject,Start date,Start time,End Time"+"\n")
for y in wochentag:
    wochenzahl = int(wochentag.index(y))
    formatierung(y, wochenzahl)
file.close()


#print("Dienst"+","+kw_format_new+","+Montag[0][1]+","+Montag[0][3])
#print("Dienst"+","+kw_format_new+","+Dienstag[0][1]+","+Dienstag[0][3])
#print("Dienst"+","+kw_format_new+","+Mittwoch[0][1]+","+Mittwoch[0][3])
#print("Dienst"+","+kw_format_new+","+Donnerstag[0][1]+","+Donnerstag[0][3])
#print("Dienst"+","+kw_format_new+","+Freitag[0][1]+","+Freitag[0][3])
#print("Dienst"+","+kw_format_new+","+Samstag[0][1]+","+Samstag[0][3])
#print("Dienst"+","+kw_format_new+","+Sonntag[0][1]+","+Sonntag[0][3])