#!/usr/bin/env python3

##import time

inputFile = open('példa.txt', 'r')


# ######  BEOLVASÁS  #######


# -- negyedik megoldás --
# itt karakterenként (byte-onként) olvassuk be
##while True:
##    letter = inputFile.read(1)
##    if letter:
##        print(letter, end='', flush = True)
##        time.sleep(.1)
##    else:
##        break


# --- ötödik megoldás ---
# itt (is) soronként történik a beolvasás, viszont
# egy listába teszi a beolvasott sorokat.

text = inputFile.readlines()
outputList = []
for line in text:
    outputList.append(line.strip())
print(outputList)


# ######  KIÍRÁS  #######

outputFile = open('példa_output.txt', 'w')
outputFile.write("Ez a kimeneti fájl\n")
for element in outputList:
##    outputFile.write(element + '\n')
    print(element, file=outputFile)
    
inputFile.close()
outputFile.close()
