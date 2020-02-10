#!/usr/bin/env python3

inputFile = open('names.txt')
for row in inputFile:
    data = row
    print(data, end='')
inputFile.close()
