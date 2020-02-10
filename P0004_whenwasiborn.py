#!/usr/bin/env python3
import math

name = input('What\'s your name? ')
age = int(input('And how old are you? '))

year_of_birth = 2020 - age
print(name, ', you were born in ', year_of_birth, '.', sep = '')

