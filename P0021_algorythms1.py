#!/usr/bin/env python3

numList = [2, 5, 2, 9, 5, 8, 8, 2, 7, 9, 1]
print('szám lista elemei:', numList)
# sum

summ = 0;
for num in range(1, 101):
    summ += num
print('A számok összege 1 - 100-ig:', summ)
print('szám lista összege:', sum(numList))

# average

summ = 0;
count = 0
for num in range(1, 101):
    summ += num
    count += 1
print('A számok átlaga 1 - 100-ig:', summ/count)
print('szám lista átlaga:', sum(numList)/len(numList))

# multiply

product = 1;
for num in range(1, 101):
    product *= num
print('A számok szorzata 1 - 100-ig:', product)


# characters (step by step)

text = ''
characters = ['E', 'n', 'n', 'y', 'i']
for character in characters:
    text += character
print(text)

print('123'.join('4567'))
print(''.join(characters))


