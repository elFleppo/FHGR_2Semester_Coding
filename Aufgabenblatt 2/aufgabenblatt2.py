#Author: Stiafen Flepp
#Date: 01.03.2023
#Content: Aufgabenblatt 2
def tail_fakultaet(n):
    def h(m,n):
        if n == 0:
            return m
        else:
            return h(n*m, n-1)
    return h(1,n)
print(tail_fakultaet(5))



#Aufgabe 7
liste = [1, 1.32, -2.3, 5.8, 0.927]
vierfaches = lambda a: a*4
drittewurzel = lambda a: a**(1/3)
summeliste = lambda a: sum(a)
print(vierfaches(5))
print(drittewurzel(27))
print(summeliste(liste))


#Aufgabe 8
counter = 0
def vielfaches(x):
    global counter
    counter = counter+1
    return 2*x

def quadratfunktion(x):
    global counter
    counter=counter+1
    return x*x

def fakultaetsfunktion(x):
    global counter
    counter = counter+1
    if x == 0:
        return 1
    else:
        return x * fakultaetsfunktion(x - 1)

#Funktion höchster Ordnung gibt nur den Counter zurück welcher von den Funktionen gesetzt wurde
def HighestOrda(function):

    return counter





print(HighestOrda(fakultaetsfunktion(5)))
#Ausgabe 6
#Aufgabe 9

anonymefakultaet = lambda n: n-1 + abs(n-1) and anonymefakultaet(n-1)*n or 1
print(anonymefakultaet(5))