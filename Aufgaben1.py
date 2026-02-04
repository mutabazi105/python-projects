'''#1
print("Hallo Welt")

name = "Bernard Mutabazi"
print("Mein Name ist:", name)

alter = 25
print("Name:", name, "\nAlter:", alter)

# 4. Ausgabe mit \n und \t
#print("Zeile 1\n\tZeile 2 mit Tab\nZeile 3") '''



 
# 5. Datentypen: Integer, Float, String, Boolean
a_int = 5
b_float = 3.14
text = "Hallo"
wahrheit = True

# 6. Zwei Zahlen addieren und Ergebnis ausgeben
#zahl1 = 10
#zahl2 = 20
summe = a_int + b_float
print(text,"\t This is the Summe of",a_int ,'and', b_float,'is:', summe)

# 7. Typ jeder Variablen ausgeben
print("Typ von a_int:", type(a_int))
print("Typ von b_float:", type(b_float))
print("Typ von text:", type(text))
print("Typ von wahrheit:", type(wahrheit))

# 8. input() für eine Zahl
benutzer_zahl = int(input("Bitte eine Zahl eingeben: "))
benutzer_text= str(input('please Enter your Name: '))
ergebnis = benutzer_zahl*2
print('Hallo ', benutzer_text,'Das Doppelte deiner Zahl ist:', ergebnis)

print('The typ für Benutzer_zahl ist:',type(benutzer_zahl))