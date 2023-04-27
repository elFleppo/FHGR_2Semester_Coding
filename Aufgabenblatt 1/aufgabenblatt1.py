#Author: Stiafen Flepp
#Date: 01.03.2023
#Content: Aufgabenblatt 1

import pandas as pd
import numpy as np
import sympy as sp
import xml.etree.ElementTree as et

#xtree = et.parse("C:/Users/Stiafen Flepp/Documents/FHGR/2-Metadata/dblp.xml/data-dblp.xml")
#xroot = xtree.getroot()

#Rekursive Funktion für Fakultät
def rekursive_fakultaet(n):

    if n == 1:
        return 1
    else:
       return rekursive_fakultaet(n-1)*n

print(rekursive_fakultaet(5))

#Binominalkoeffizient
def binominalkoeffizient(n, k):
    return rekursive_fakultaet(n)/(rekursive_fakultaet(n-k)*rekursive_fakultaet(k))

print(binominalkoeffizient(10,2))


def akermann(x,y):

    if x == 0:
        y = y+1

    if y == 0:
        return akermann(x-1, 1)
    else:
       return akermann(x-1,y),akermann(x, y-1)


print(akermann(1, 1))

#Aufgabe zum Datensatz
# a) Der Datensatz ist eine Xml Datei in welcher die Werte zwischen sogenannten "Tags" liegen.
# b) Der Datensatz hat eine Grösse von 3.53 GB
# c) Sind Kontinentale (Europa, Amerika, Asien, Afrika) Forschungstrends zu finden?
#    Gibt es Themen in welchen Papers häufiger in zusammenarbeit statt alleine geschrieben werden?
#    Welche Wörter sind besonders häufig in den Titel von Papers anzutreffen?