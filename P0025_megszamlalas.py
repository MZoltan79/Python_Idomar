#!/usr/bin/env python3

chars = ['a', 'v', 'b', 'k', 'a', 'f', 'o', 'l', 'm', 'o', 'a']

afterK = 0
countAs = 0

for char in chars:
    if char > 'k':
        afterK += 1
    if char == 'a':
        countAs += 1
print('k-nál nagyobb betűk száma:', afterK)
print(countAs, '"a" betű van a listában')

print(chars.count('a'), '"a" betű van a listában')
