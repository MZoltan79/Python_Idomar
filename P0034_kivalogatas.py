#!/usr/bin/env python3


def iseven(number):
    return number % 2 == 0


numbers = [1, 103, 56, 49, 37, 18]
evens = []
for num in numbers:
    if iseven(num):
        evens.append(num)
print('Eredeti lista:', numbers)
print('Párosak:', evens)
