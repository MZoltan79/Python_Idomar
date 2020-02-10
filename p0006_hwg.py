#!/usr/bin/env python3

name = input('Szia, hogy hívnak? ')
gender = input('Fiú vagy, avagy lány? (f/l) ')
timeOfDayH = input('Milyen napszak van? (r/du/e/é) ')

if gender == 'l':
    forName = 'Ms'
elif gender == 'f':
    forName = 'Mr'
else:
    print('Ilyen nmet sajnos nem ismerek...')
    forName = 'M?'

if timeOfDayH == 'r':
    timeOfDayE = 'morning'
elif timeOfDayH == 'du':
    timeOfDayE = 'afternoon'
elif timeOfDayH == 'e':
    timeOfDayE = 'evening'
elif timeOfDayH == 'é':
    timeOfDayE = 'night'
else:
    print('Ilyen napszakot nem ismerek...')
    timeOfDayE = 'i don\'t know'

print('Good ', timeOfDayE,' ', forName,' ', name,'!', sep='')
