#!/usr/bin/env python3

def plus5(number):
    return number + 5

def firstname(name):
    return name.split()[1]

numbers = [1, -2, -3, 4, -5, 6, 7]
names = ['Kis Aladár', 'Nagy Elemér', 'Közepes Kálmán']


# numbers2 = []
# for num in numbers:
#     numbers2.append(plus5(num))
# ehelyett lehet ezt így is:
numbers2 = list(map(plus5, numbers))


print(numbers, id(numbers))
print(numbers2, id(numbers2))

for name in names:
    print(firstname(name))

firstnames = list(map(firstname, names))
print(firstnames)
