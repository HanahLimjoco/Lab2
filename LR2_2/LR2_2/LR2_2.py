from msilib.schema import File
from pickle import TRUE

print ("File Navigator Program: \n")

"""Opens A File Using Prompt: """
inFile = input("Input a File Name: ") +".txt"
openFile = open(inFile,"r")
readlist=openFile.read()

"""Separates Each Lines in the TextFile into a List"""
listLine = readlist.split("\n")

"""Outputs Each Line Entry Once"""
print("\nList Contents: \n")
for x in listLine:
    print(x)

"""User Input for Which Line to Display"""
lineSelect = input("\nSelect A Line Number to Display: ")

"""While Loop Until Exit Value: 0 is Entered"""
while(lineSelect!="0"):
    display = listLine[int(lineSelect)-1]
    print(display)

    lineSelect = input("\nSelect A Line Number to Display: ")