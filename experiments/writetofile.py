#!/usr/bin/env python3


outputFile = open('names.txt', 'a')
fName = input('What\'s your firstname? ')
lName = input('What\'s your lastname? ')
sex = input('What\'s your gender(male/female)? ')
age = input('How old are you? ')
print(fName, lName, '-', sex, age, file=outputFile, flush = False)
outputFile.close()

