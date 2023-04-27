#Author: Stiafen Flepp
#Date: 20.04.23
#Content: Aufgabenblatt 4
import numpy as np
import imageio as img
import random as rd
from matplotlib.image import imread
def readfile(path):
   with open(path, 'r') as file:
       string = file.read()
       print(string)
readfile("text.txt")

def modifyfile(path):
    with open(path, 'r+') as file:
        new_string = ""
        #get old data so we know when the cursor needs to move back to start
        old_data = file.read()

        for i in range(len(old_data)):
            #move cursor along length of string
            current_pos = file.seek(i)
            #read single character for ord number
            character = file.read(1)
            ordnumber = ord(character)
            #set new ordnumber and generate new character
            new_ordnumber = ordnumber + 1
            new_character = chr(new_ordnumber)
            #concatenate new chars to new string for file
            new_string = new_string+new_character
        #Move cursor back to start, write and close file
        file.seek(0,0)
        file.write(new_string)
        file.close()

modifyfile("modify.txt")

def connect(path1, path2, outfile):
    with open(path1) as file1:
        data1 = file1.read()
    with open(path2) as file2:
        data2 = file2.read()

    outputdata = data1 + "\n" + data2
    with open(outfile, 'w') as outputfile:
        print("output has been written to: " +outfile)
        outputfile.write(outputdata)

connect(path1="test1.txt", path2="test2.txt", outfile="connectOutput.txt")


def countColors(image):
    rgb_data = img.imread('facing_python.jpg')
    print(np.shape(rgb_data))
    colors = np.mean(rgb_data, axis=2)
    print(colors, np.shape(colors))
    print(np.unique(colors), np.shape(np.unique(colors)))
    color_arr = np.unique(colors)
    sum_dict = {}


    for color in color_arr:
        sum_dict[color] = (colors == color).sum()

    #Anzahl Vorkommen für die Top 10 Farben
    result = dict(sorted(sum_dict.items(), key=lambda x: x[1], reverse=True)[:10])
    topvalues = result.keys()
    for color in colors:
        if color not in topvalues:
            color = result[rd.randint(0,9)]
    print(colors)
    print(result)
countColors("facing_python.jpg")

