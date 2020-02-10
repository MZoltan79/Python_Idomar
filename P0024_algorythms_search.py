#!/usr/bin/env python3

# search - keresés

fruits = ['banán', 'körte', 'szilva', 'alma', 'barack', 'narancs']

item = input('Mit keressünk? ')
# 1. megoldás:
	
for fruit in fruits:
	if fruit == item:
		print('Megvan! a ', fruits.index(item)+1, '.', sep='')
		break
else:
	print('Nincs ilyen elem.')
	
#2. megoldás:
		
	
for i in range(len(fruits)):
	if fruits[i] == item:
		print('Megvan! a ', i+1, '.', sep='')
		break
else:
	print('Nincs ilyen elem.')	

#3. megoldás:

if item in fruits:
	print('Megvan, a ',fruits.index(item)+1, '.', sep='')
else:
	print('Nincs ilyen elem')