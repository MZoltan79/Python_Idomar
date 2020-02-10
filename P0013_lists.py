#!/usr/bin/env python3

heros = []
hero = None
print('This program stores names.\nTo stop input, hit ENTER without any text!')
while hero != '':
    hero = input('please type a fairytale hero\'s name here:... ')
    if hero: # this line equals: if hero != ''  - because '' means False!!!
        heros.append(hero)
print(heros)
