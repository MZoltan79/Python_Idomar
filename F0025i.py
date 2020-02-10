#!/usr/bin/env python3

#hány olyan szó van az alábbi listában ami f-fel kezdődik és e-re végződik? 

listOfWords = ['fele', 'fölfele', 'ferde', 'felette', 'zabkeksz']
begins = 'f'
ends = 'e'
count = 0
for i in range(len(listOfWords)):
    if listOfWords[i][0] == begins and listOfWords[i][len(listOfWords[i])-1] == ends:
        count += 1
print(count, 'szó volt ami "f"-el kezdődik és "e"-vel végződik.')

