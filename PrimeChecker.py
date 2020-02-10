#!/usr/bin/env python3

import math

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

number = int(input('Adj meg egy természetes számot, megmondom prím-e. '))
if isPrime(number):
    print('A szám prím.')
else:
    print('A szám nem prím.')



