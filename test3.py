#print('Hanno'+'ver')# Das Pluszeichen hier ist ein Konkatenationsoperation
#print(1+2) #Das Pluszeichen hier ist ein additionsoperator

#CONCATENATION - Konkatenation

#print(10+12)
#print(14-13)
#print(11*2)
#print(3**2)
#print(10/2)
#print(15%2)
#print(type(True)) #ein fonktion in andere function

#1
print("Hallo Welt")

name = "Dein Name"
print("Mein Name ist:", name)

alter = 25
print("Name:", name, "\nAlter:", alter)

# 4. Ausgabe mit \n und \t
print("Zeile 1\n\tZeile 2 mit Tab\nZeile 3")
 
# 5. Datentypen: Integer, Float, String, Boolean
a_int = 5
b_float = 3.14
text = "Hallo"
wahrheit = True

# 6. Zwei Zahlen addieren und Ergebnis ausgeben
#zahl1 = 10
#zahl2 = 20
summe = a_int + b_float
print("Summe:", summe)

# 7. Typ jeder Variablen ausgeben
print("Typ von a_int:", type(a_int))
print("Typ von b_float:", type(b_float))
print("Typ von text:", type(text))
print("Typ von wahrheit:", type(wahrheit))

# 8. input() für eine Zahl
benutzer_zahl = int(input("Bitte eine Zahl eingeben: "))
ergebnis = benutzer_zahl * 2
print("Das Doppelte deiner Zahl ist:", ergebnis)


# Arithmetische Operatoren
print("3 + 4 =", 3 + 4)
print("10 - 2 =", 10 - 2)
print("5 * 3 =", 5 * 3)
print("9 / 2 =", 9 / 2)

# Vergleich zweier Zahlen
zahl1 = 7
zahl2 = 7
if zahl1 == zahl2:
    print("Die Zahlen sind gleich.")
else:
    print("Die Zahlen sind unterschiedlich.")

# Verwendung von and und or mit True/False
print("True and False:", True and False)
print("True or False:", True or False)

# Komplexes if-Statement mit multiple Bedingungen
alter = 20
ist_student = True
if (alter > 18 and ist_student) or not (alter < 18):
    print("Bedingung erfüllt")
else:
    print("Bedingung nicht erfüllt")

# Funktionen: len(), input(), range(), sum(), abs(), sorted()
# len() auf einem String
text = "Hallo Welt"
print("Länge des Strings:", len(text))

# sum() auf einer Liste
zahlen = [1, 2, 3, 4]
print("Summe der Liste:", sum(zahlen))

# for Schleife mit range()
print("Schleife mit range(1,10,2):")
for i in range(1, 10, 2):
    print(i)

# input() zum Einlesen von Zahlen
zahl_a = int(input("Gib eine Zahl ein: "))
zahl_b = int(input("Gib eine weitere Zahl ein: "))
differenz = abs(zahl_a - zahl_b)
summe_zwei = sum([zahl_a, zahl_b])
print("Absolute Differenz:", differenz)
print("Summe:", summe_zwei)

# Liste von Zahlen einlesen, sortieren
liste = []
anzahl_zahlen = int(input("Wie viele Zahlen möchtest du eingeben? "))
for _ in range(anzahl_zahlen):
    zahl = int(input("Gib eine Zahl ein: "))
    liste.append(zahl)
sortierte_liste = sorted(liste)
print("Sortierte Liste:", sortierte_liste)

# Überprüfen, ob alle Zahlen positiv sind, und ob mindestens eine positive Zahl existiert
positive = [z > 0 for z in liste]
print("Alle Zahlen positiv?", all(positive))
print("Mindestens eine positive Zahl?", any(positive))
Regenerieren
Kopieren
Gute Antwort
Schlechte Antwort

