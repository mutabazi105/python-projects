import pandas
import numpy
import sys
print(sys.version)
print('Pandas:', pandas .__version__)
print('Numpy:', numpy .__version__)

'''print("10+12")
print(10+12)
print(15/5)
print(2*3)
print(2**3)
print("Hanno","ver")
print("Hanno"+"ver")
print(type(print))
print(type(12.0))
print(type(12))"""

#print('Hallo werlt')

"""einkaufsliste=['Joghrt','Brot', True]
text=12

print(einkaufsliste)
print(text)"""

#suweisung--> assignment

#variablei='wert'
#print(variablei)

#print(type(variablei))

"""tupel=(1,2,3,4)
liste1=[1,2,3,4]
liste1.append(5) 

print(tupel)
print(liste1)"""

"""dictionary={
    'Apfel':'Apple',
    'Birne':'Pear',
    'Wasswermelone':'Watermelon'
}

#print(dictionary[])
"""

"""blutzuckerwerte={
    'Max':78,
    'Leon':57,
    'Lena':110
 
}"""

#print('Ausgabe: ' + str(blutzuckerwerte['Leon'])+ ' Mmol/dm³')

#print(blutzuckerwerte.value())
#print(blutzuckerwerte.items())

#print(dictionary.keys())
#print(dictionary.values())
#print(dictionary.items())


buchstbn= ['a','b','c', 'd']
wort='Bäume'
"""var1=len(buchstbn)
var2=len(wort)
print(var1)
print(var2)"""

#print(buchstbn[0])
#print(wort[0])

"""richtungen= ['links/left','mitte/center','rechts/right']
print(richtungen[0])
print(richtungen[1])
print(richtungen[2])
print(richtungen[-1])
print(richtungen[-2])
print(richtungen[-3])"""

#a=int(input('Bitte hier einen Wert eingeben:'))
#b=100
#c=a+b
#print(c)

#for i in range(0,55,5):
#    print(i(0))

#Verwendung von Inputfunktion+explizite typkonvertierung mit int() 
variable=int(input('geben sie eine Zal'))
a=100
c=variable+a
print(c)

#for-schleife+range(start,stop,step)
for i in range(1,10,2):

    print(i+1)
#sorted für die Liste[7,3,1,9,8,2,4]
x=[7,3,1,9,8,2,4]
#mit mit reverse True, reverse False und kein optionaler Parameter '''


'''#03

# Arithmetische Operatoren
print("3 + 4 =", 3 + 4)
print("10 - 2 =", 10 - 2)
print("5 * 3 =", 5 * 3)
print("9 / 2 =", 9 / 2)

# Vergleich zweier Zahlen
zahl1 = 7
zahl2 = 3
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
    print("Bedingung nicht erfüllt") '''

# 04

# Funktionen: len(), input(), range(), sum(), abs(), sorted()
# len() auf einem String
'''text = "Hallo Welt"
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
print("Mindestens eine positive Zahl?", any(positive)) '''
