#!/usr/bin/env python3

# mutable variable

a1 = [1, 2]
b1 = a1

a1[0] = 'abc'
print(a1, b1)

# a list mutable, azaz ha ugyanarra a referenciára 2
# hivatkozás mutat, és az egyiket változtatom, mind
# a 2 megváltozik.

# ezért 'másolni' kell!

a2 = [1, 2]
b2 = a2[:] # vagy list(a2)

a2[0] = 'abc'
print(a2, b2)

# immutable variables

a = 3
b = a
print(a, b, a == b, a is b)



a = 4
print(a, b)



# érdekesség, hogy a python optimalizációs okok
# miatt eleve betölt bizonyos objektumokat a 
# memóriába (a számokat pl. -5 - 256-ig).
# az alábbi pár sor ezt hivatott szemléltetni:
	
a = -5
b = -5
while a is b:
	a += 1
	b += 1
	print('a = ', a, ', b = ', b, ', a == b: ', a == b, ', a is b: '\
	, a is b, sep = '')
		