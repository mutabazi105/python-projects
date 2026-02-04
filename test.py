import matplotlib.pyplot as plt


'''#name=input("What is your name? ")
#print(f"Hello,{name}! Welcome to Python.")

# 27.10.2021

a=['Banane','Apfel','Birne','Quitte']
b=['Banane','Apfel','Birne','Quitte']

#c=a.extend(b)
#print(c)

a=a+['Orange'] # Das funktioniert genau wie append  

print(a)

a=a[:2]+['Mango']+ a[2:] # Um einen Wrt mitten in die Liste zu addieren 
print(a)

#1. a[:2] - Alle Werte vom Beginn bis Position2 
#2. den Wert Mango
#3. a[2:] - ab  Pos. 2 bis Ende der Liste 
#4. so bekommen wir den Wert Mango an Pos 2.

a[1]='Mango' # Option 2 - Ersetzt den Wert 'Apfel' durch Mango
a.insert(1,'Mango') # Option 3 - schiebt den Wert 'Apfel' eine Stelle witer, damit für 'Mango 
#Platz gemacht wird 

print(a)'''


'''a=[1,2,3,4,5]
print (a)

del a # Del Keyword löscht die Liste vom Speicherplatz

del a[:] # Löscht alle Elemente aber nicht die Liste selbst 
del a[0] # Löscht des Element mit Index 0

list.remove('b') # Entfernt das Element 'b'

print(a)'''



'''
a= [

   ['a','b']
   ['c','d']
   ['e','f']
   ]

print(a[0][0])
print(a[1])
print(a[2][0])
print(a[1:])

# a. a
# b. c,d
# c. e
# d. [c,d],[e,f]'''



#Aufgabe
''' Bitte geben sie mithilfe von Indites nur die folgenden werte aus:
a, ['Banane']
b. ['Qute'] Beides negative und positive Indizes anwenden 
c. ['Apfel, Birne']
d. ['Banane','Apfel#]'''

'''print(a[1:2])

a[1]='Mango' # option 1 - Ersetzt den wert 'Apfel' durch Mango

a.insert(1,'Mango') #Option 2 - Schiebt den wert 'Apfel' eine stelle witer, damit für 'Mango
#Platz gemacht wird'''

'''

einkfliste={'item1':['Schuhe',180],
             'item2':['Hemd', 200],
             'item3':['Gürtel',50]
             

             }
#print(einkfliste['item1'])

einkfliste_updated={
                  'Schue':{'Preis',180},
                  'Hemd':{'Preis', 200},
                  'Gürtel':{'Preis',50}
             
            
             }
#print(einkfliste['item1'])

print(einkfliste_updated['Gürtel']) '''

'''

gebäude={
                  'Abteilung A':{'Raum1','Computerraum', 'Raum2', ''},
                  'Abteilung B':{'Rum2', 200},
                  'Abteilung C':{'Preis',50}
             
            
             }

'''




'''def hello():
    print('Hi, was kann ich für dich tun ')

def einspluseins():
    print(1+1)

hello()
einspluseins()'''


'''def bmi(m,l): # Funktionskopf, Name der Funktion BMI| Zwei Parameter m - Gewicht & 1 - Größe
    erg= round(m/(1**2)) # Funktionsrumpf Teil I
    return erg #Funktionsrumpf Teil II

print(bmi(100,1.76))
print(bmi(78,1.76))'''


'''kilos=float(input('Geben Sie Körpergröße in kg ein:'))
meter=float(input('Geben Sie Körpergröße in meter ein:'))

def bmi(m,l):
    erg=round(m/(1**2),2)
    return erg

print('Das BMI Wert ist', bmi(kilos,meter))
result=bmi(kilos,meter)

print(result)


if result <18.5:
    print('Untergewichtig')

elif result >=18.5 and result<30:
    print('Normalgewichtig')

else:
    print('Ubergewichtig')
    '''



'''x=100000

if x==10:
    print('X  ist klein gleich 10 ')

elif x>=11 and x<20:
    print('X ist größer als 10 aber kleiner als 20')

else:
    print('x ist größer als 20')
'''


'''letters='DEUTSCHLAND'
liste=['a','b','c','d']

for letter in letters:
    print(letters)

for letter in letters:
    #print(liste)

for i in liste:
    print(i)'''


'''lengths=['1.75','1.73','1.78','1.76','1.55']

i=0
while lengths[i]<1.76:

    print(lengths[i])
    i=i+1'''



'''#cart=[("Laptop", 1000),("Coffee", 5),("Book", 15), ("")]


einkauf=[("Laptop", 2000),
         ("Tastatur", 50),
         ("Maus", 20),
         ("Tasche", 10)]

for index, (produkt, preis) in enumerate (einkauf, start=1):
    if preis>1000:
        rabbat=0.25
    else:
        rabbat=0.1

    endpreis=preis*(1-rabbat)

print(f"{index} - {produkt} - ${preis}= ${endpreis: .2f} - Rabbat: {rabbat*100: .0f}%")

print(f"Hallo ich bin  Abid und ich bin {30} Jahre alt")

#print("Hallo ich bin  Abid und ich bin 30 Jahre alt")'''




'''x=[1,2,3,4,5]
y=[2,4,6,8,10]

plt.plot(x,y)
plt.xlabel('x=Achse')
plt.ylabel('y=Achse')
plt.title('Grafik')

plt.show()'''
