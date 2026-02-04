# 01
import random
zahl = 42
kommazahl = 3.14
text = 'Hallo Welt'
wahrheit = True

print(type(zahl), '\n', type(kommazahl),
      '\n', type(text), '\n', type(wahrheit))


# Aufgabe 2: Umwandlung von Datentypen
x = 10
x_str = str(x)

print(x)        # Ausgabe: 10
print(x_str)    # Ausgabe: "10"

zahl = int("5")
ergebnis = zahl + 5
print(ergebnis)


# Aufgabe 3: Benutzer-Eingaben und Datentypen
alter = int(input("Wie alt bist du? "))
in_fuenf_jahren = alter + 5

print("In 5 Jahren bist du", in_fuenf_jahren, "Jahre alt.")


# Aufgabe 4: Eine einfache Klasse definieren
class Auto:
    def __init__(self, marke, baujahr, farbe):
        self.marke = marke
        self.baujahr = baujahr
        self.farbe = farbe


# Ein Auto-Objekt erzeugen
auto1 = Auto("BMW", 2015, "schwarz")

# Informationen ausgeben
print("Marke:", auto1.marke)
print("Baujahr:", auto1.baujahr)
print("Farbe:", auto1.farbe)


# Aufgabe 5: Zwei Auto-Objekte vergleichen:

# Klasse Auto definieren
class Auto:
    def __init__(self, marke, baujahr, farbe):
        self.marke = marke
        self.baujahr = baujahr
        self.farbe = farbe

# Funktion zum Vergleich der Autos


def welches_auto_neuer(auto1, auto2):
    if auto1.baujahr > auto2.baujahr:
        print(auto1.marke, "ist neuer.")
    elif auto2.baujahr > auto1.baujahr:
        print(auto2.marke, "ist neuer.")
    else:
        print("Beide Autos sind gleich alt.")


# Zwei Auto-Objekte erstellen
auto1 = Auto("Audi", 2018, "rot")
auto2 = Auto("Mercedes", 2020, "silber")

# Vergleich aufrufen
welches_auto_neuer(auto1, auto2)


# Ausgabe:

# Mercedes ist neuer.


# Aufgabe 1: Liste anlegen und bearbeiten
zahlen = [3, 6, 1, 9]

# Erstes, drittes und letztes Element ausgeben
print(zahlen[0])   # erstes Element → 3
print(zahlen[2])   # drittes Element → 1
print(zahlen[-1])  # letztes Element → 9

# Zahl 5 anhängen und sortieren
zahlen.append(5)
zahlen.sort()

print(zahlen)      # Ausgabe: [1, 3, 5, 6, 9]

# Aufgabe 2: Dictionary mit Personendaten
person = {"name": "Sara", "alter": 28, "stadt": "Berlin"}

# Alle Schlüssel ausgeben
print(person.keys())

# Alle Werte ausgeben
print(person.values())

# Alter ändern
person["alter"] = 29

print(person)   # Ausgabe: {"name": "Sara", "alter": 29, "stadt": "Berlin"}


# Aufgabe 3: Tuple unveränderlich verstehen

wochentage = ("Mo", "Di", "Mi", "Do", "Fr")


# Warum kann man den ersten Eintrag nicht ändern?

# → Weil ein Tuple unveränderlich (immutable) ist.
# Das bedeutet:

# Man kann keine Werte löschen,

# keine Werte hinzufügen,

# und keine vorhandenen Werte ändern.

# Beispiel (das würde einen Fehler verursachen):

wochentage[0] = "Montag"   # ❌ Nicht erlaubt, da Tuple unveränderlich

# Aufgabe 4: Mehrdimensionale Daten
klassenbuch = [["Ali", 1], ["Eva", 2], ["Luis", 1]]

# Note von Eva ausgeben
print(klassenbuch[1][1])   # Ausgabe: 2


# Erklärung:

# klassenbuch[1] → ["Eva", 2] (zweite Person)

# klassenbuch[1][1] → 2 (Evas Note)


# Aufgabe 5: Dictionary mit Liste als Wert
stundenplan = {"Montag": ["Mathe", "Deutsch"]}

# Fach "Englisch" für Montag hinzufügen
stundenplan["Montag"].append("Englisch")

print(stundenplan)


# Ausgabe:

{'Montag': ['Mathe', 'Deutsch', 'Englisch']}


# Aufgabe 1: Listen-Methoden praktisch
farben = ["rot", "blau", "grün"]

# Schritt 1: "gelb" anhängen
farben.append("gelb")

# Schritt 2: "violett" auf Position 1 einfügen
farben.insert(1, "violett")

# Schritt 3: letztes Element entfernen
farben.pop()

print(farben)


# Ausgabe:

['rot', 'violett', 'blau', 'grün']

# Aufgabe 2: Dictionary-Methoden üben
auto = {"marke": "Audi", "farbe": "schwarz"}

# Wert für "marke" ausgeben
print(auto.get("marke"))

# Farbe ändern
auto.update({"farbe": "weiß"})

# Alle Schlüssel ausgeben
print(auto.keys())

print(auto)


# Ausgabe:

# Audi
# dict_keys(['marke', 'farbe'])
# {'marke': 'Audi', 'farbe': 'weiß'}

# Aufgabe 3: Eigene Begrüßungsfunktion
def begrüßung(name):
    print("Hallo,", name + "!")


# Aufrufe
begrüßung("Sara")
begrüßung("Ali")
begrüßung("Tom")

# Aufgabe 4: Listenfunktionen verwenden: to use
zahlen = [2, 4, 6]

print(len(zahlen))   # Länge der Liste → 3
print(sum(zahlen))   # Summe → 12
print(max(zahlen))   # Größter Wert → 6


# Aufgabe 5: Prüffunktion „Wert in Liste?“
def ist_in_liste(wert, liste):
    return wert in liste


# Beispielaufrufe
zahlen = [1, 3, 5, 7]

print(ist_in_liste(3, zahlen))   # True
print(ist_in_liste(4, zahlen))   # False


# Aufgabe 1: Funktion ohne return
def drucke_zahl(x):
    print("Die Zahl ist:", x)


# Beispielaufrufe
drucke_zahl(5)
drucke_zahl(12)

# Aufgabe 2: Funktion mit return


def verdopple(x):
    return x * 2


# Beispielaufrufe
print(verdopple(3))   # Ausgabe: 6
print(verdopple(10))  # Ausgabe: 20


# Aufgabe 3: Multiplikationsfunktion zweier Zahlen
def multipliziere(a, b):
    return a * b


# Beispiel:
ergebnis = multipliziere(4, 7)
print(ergebnis)   # Ausgabe: 28

# Aufgabe 4: Gerade-Zahl-Prüfer


def ist_gerade(n):
    return n % 2 == 0


# Beispiele:
print(ist_gerade(4))   # True
print(ist_gerade(9))   # False


# Aufgabe 1: Volljährigkeit prüfen
alter = int(input("Wie alt bist du? "))
if alter >= 18:
    print("Du bist volljährig")
else:
    print("Minderjährig")

# Aufgabe 2: Zwei Zahlen vergleichen
a = int(input("Zahl a: "))
b = int(input("Zahl b: "))
if a > b:
    print("a ist größer")
elif b > a:
    print("b ist größer")
else:
    print("Beide Zahlen sind gleich")

# Aufgabe 3: Doppelte Bedingung (and)
zahl = int(input("Gib eine Zahl ein: "))
if zahl % 2 == 0 and zahl > 10:
    print("Die Zahl ist gerade und größer als 10")

# Aufgabe 4: Alternative Bedingung (or)
name = input("Name: ")
stadt = input("Stadt: ")
if name == "" or stadt == "":
    print("Bitte fülle alle Felder aus")

# Aufgabe 5: Notenstufen mit elif
note = int(input("Schulnote (1-5): "))
if note == 1:
    print("Sehr gut")
elif note == 2:
    print("Gut")
elif note == 3:
    print("Befriedigend")
elif note == 4:
    print("Ausreichend")
elif note == 5:
    print("Mangelhaft")
else:
    print("Ungültige Note")

# Thema 6: for-Schleife
# Aufgabe 1: Liste ausgeben
obst = ["Apfel", "Banane", "Kirsche", "Mango", "Pfirsich"]
for item in obst:
    print("Obst:", item)

# Aufgabe 2: Summe aller Listenelemente
zahlen = [4, 6, 12, 3]
summe = 0
for zahl in zahlen:
    summe += zahl
print("Die Summe ist:", summe)

# Aufgabe 3: Ein Wort buchstabieren
wort = input("Gib ein Wort ein: ")
for buchstabe in wort:
    print(buchstabe)

# Aufgabe 4: Gerade Zahlen herausfiltern
zahlenreihe = list(range(1, 21))
for zahl in zahlenreihe:
    if zahl % 2 == 0:
        print("Gerade:", zahl)

# Aufgabe 5: Neue Liste mit verdoppelten Werten
werte = [1, 3, 5, 7]
neu = []
for w in werte:
    neu.append(w * 2)
print(neu)

# Thema 7: for in range() und enumerate()
# Aufgabe 1: Zahlen 1-10
for i in range(1, 11):
    print(i)

# Aufgabe 2: Jede zweite Zahl bis 20
for i in range(0, 21, 2):
    print(i)

# Aufgabe 3: Index & Name (enumerate)
namen = ["Ana", "Ben", "Cem"]
for index, name in enumerate(namen):
    print(f"{index} - {name}")

# Aufgabe 4: Nur Elemente mit geradem Index
farben = ["rot", "blau", "grün", "gelb", "lila", "pink"]
for i in range(0, len(farben), 2):
    print(farben[i])

# Aufgabe 5: Rückwärts zählen
for i in range(10, -1, -1):
    print(i)

# Thema 8: Endlose while True-Schleife
# Aufgabe 1: „Hallo“ fünfmal
count = 0
while True:
    print("Hallo")
    count += 1
    if count == 5:
        break

# Aufgabe 2: Name abfragen bis „Stopp“
while True:
    name = input("Wie heißt du? ")
    if name == "Stopp":
        break
    print("Hallo,", name + "!")

# Aufgabe 3: Zahl hochzählen bis 10
n = 0
while True:
    n += 1
    if n == 10:
        print("Fertig")
        break

# Aufgabe 4: Einfaches Zahlenratespiel
zufall = random.randint(1, 20)
versuche = 0

while True:
    tipp = int(input("Rate die Zahl (1-20): "))
    versuche += 1
    if tipp < zufall:
        print("Zu niedrig")
    elif tipp > zufall:
        print("Zu hoch")
    else:
        print("Richtig! Versuche:", versuche)
        break

# Aufgabe 5: Quizfrage wiederholen
while True:
    antwort = input("Wie heißt die Hauptstadt von Deutschland? ").strip()
    if antwort.lower() == "berlin":
        print("Korrekt!")
        break

# Thema 9: Bedingte while-Schleife
# Aufgabe 1: Zahl < 5 hochzählen
zahl = 0
while zahl < 5:
    print(zahl)
    zahl += 1

# Aufgabe 2: Eingabe > 100 erzwingen
zahl = int(input("Gib eine Zahl > 100 ein: "))
while zahl <= 100:
    zahl = int(input("Bitte erneut eingeben (>100): "))
print("Danke!")

# Aufgabe 3: Solange „ja“
while True:
    antwort = input("Willst du weitermachen? (ja/nein) ").lower()
    if antwort == "ja":
        print("Weiter geht’s!")
    else:
        break

# Aufgabe 4: Teilbarkeit durch 2
num = 64
while num % 2 == 0:
    print(num)
    num //= 2

# Aufgabe 5: Passwort prüfen
passwort = "geheim"
while True:
    eingabe = input("Passwort: ")
    if eingabe == passwort:
        print("Zugang erlaubt")
        break

# Thema 10: while mit break, continue, Iterable
# Aufgabe 1: Liste mit while durchlaufen
tiere = ["Hund", "Katze", "Maus"]
i = 0
while i < len(tiere):
    print(tiere[i])
    i += 1

# Aufgabe 2: break, wenn Wert 0
werte = [5, 7, 0, 3]
i = 0
while i < len(werte):
    if werte[i] == 0:
        break
    print(werte[i])
    i += 1

# Aufgabe 3: continue, wenn None
daten = [3, None, 4, None, 7]
i = 0
while i < len(daten):
    if daten[i] is None:
        i += 1
        continue
    print(daten[i])
    i += 1

# Aufgabe 4: Nur ungerade Zahlen ausgeben
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# Aufgabe 5: Iterator per iter()
farben = ["rot", "grün", "blau"]
it = iter(farben)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# Thema 10 Extra: Aufgabe 5 (Funktion ohne Rückgabe / kleine Textgrafik)


def rechteck():
    print("*****")
    print("*****")
    print("*****")


rechteck()
