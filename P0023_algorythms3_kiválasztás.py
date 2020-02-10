#!/usr/bin/env python3

leaders = ['Álmos', 'Előd', 'Ond', 'Kond', 'Tas', 'Huba', 'Töhötöm']

name = input('Kit keresel? ')

for i in range(len(leaders)):
    if leaders[i] == name:
        print(name, ' a(z) ', i+1, '. a listában.', sep='')
        break
else:
    print(name, 'nincs a listában.')

##MÁSIK MEGOLDÁS
print(name, ' a(z) ', leaders.index(name)+1, '. a listában.', sep='')

