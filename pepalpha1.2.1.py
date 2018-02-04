## Copyright Pintarich Christopher						  ##
## Personal Einsatzplanwandler in CSV für Google Kalender ##
## Für Nutzungsinformationen, siehe Anleitung			  ##
############################################################

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
    for line in file:
        daycutter(line)

## Wandelt das 24 Stunden Format in ein 12 Stunden Format
def daytime(t_zeit, tag_in):
    container = []
    if t_zeit < 25 and t_zeit >= 13:
        t_zeit_conv = str(t_zeit-12)
        container.append(t_zeit_conv)
        container.append(tag_in)
        container.insert(2," PM")
        return str(container[0])+str(container[1])+str(container[2])
    elif t_zeit <= 11:
        t_zeit_conv = str(t_zeit)
        container.append(t_zeit_conv)
        container.append(tag_in)
        container.append(" AM")
        return str(container[0])+str(container[1])+str(container[2])
    elif t_zeit == 12:
        t_zeit_conv = str(t_zeit)
        container.append(t_zeit_conv)
        container.append(tag_in)
        container.insert(2," PM")
        return str(container[0])+str(container[1])+str(container[2])

def kalenderwoche(year, kw):
    fourth_of_january = datetime.date(year,1,4).weekday()
    first_monday = datetime.date(year,1,4-fourth_of_january)
    monday_of_kw = first_monday + datetime.timedelta(days=(kw-1)*7)
    data = []
    for i in range(7):
        d = monday_of_kw + datetime.timedelta(days=i)
        data.append("%s.%s" % (d.day, d.month))
    return data

## Dateprint gibt die Daten aus und Datewrite schreibt die Daten in das File "pepweek.csv"
class Dateprint():
    def dater(self, dat, ctag, g):
        print("Dienst"+","+g+","+dat(int(ctag[0][1][:-3]), str(ctag[0][1][2:]))+","+g+","+dat(int(ctag[0][3][:-3]), str(ctag[0][3][2:]))++",,true,false,,,,CCC"+"\n")
class Datewrite():
    print("Der PEP-Eintrag wurde geschrieben")
    def dater(self, dat, ctag, g):
        file.write("Dienst"+","+g+","+dat(int(ctag[0][1][:-3]), str(ctag[0][1][2:]))+","+g+","+dat(int(ctag[0][3][:-3]), str(ctag[0][3][2:]))+",,true,false,,,,CCC"+"\n")
##
w = Datewrite()
##
## wkek gleicht ab ob der Tag mit der Dateneingabe übereinstimmt
def wkek(wo_tag, s):
        if "Montag" == wo_tag:
            if "FREI" != Montag[0][3]:
                w.dater(daytime, Montag, s)
        elif "Dienstag" == wo_tag:
            if "FREI" != Dienstag[0][3]:
                w.dater(daytime, Dienstag, s)
        elif "Mittwoch" == wo_tag:
            if "FREI" != Mittwoch[0][3]:
                w.dater(daytime, Mittwoch, s)
        elif "Donnerstag" == wo_tag:
            if "FREI" != Donnerstag[0][3]:
                w.dater(daytime, Donnerstag, s)
        elif "Freitag" == wo_tag:
            if "FREI" != Freitag[0][3]:
                w.dater(daytime, Freitag, s)
        elif "Samstag" == wo_tag:
            if "FREI" != Samstag[0][3]:
                w.dater(daytime, Samstag, s)
        elif "Sonntag" == wo_tag:
            if "FREI" != Sonntag[0][3]:
                w.dater(daytime, Sonntag, s)

##Wandelt das Datum in ein amerikanisches Format
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

##Schreibt die fertige "pepweek.csv"
file = open("../pepkw.csv", "w")
file.write("Subject,Start Date,Start Time,End Date,End Time,All Day Event,Reminder On/Off,Reminder Date,Reminder Time,Meeting Organizer,Description"+"\n")
for y in wochentag:
    wochenzahl = int(wochentag.index(y))
    formatierung(y, wochenzahl)
file.close()


