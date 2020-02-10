#!/usr/bin/env python3

enough = 'n'
while True:
    print('5 + 5 = 10')
    enough = input('most már érted? (i/n)')
    if(enough == 'i'):
        break

for i in range(-1, -11, -1): #ugye figyelsz a -11-re a -10 helyett?!
    print(i**3)
