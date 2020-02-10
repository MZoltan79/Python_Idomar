#!/usr/bin/env python3

##print(1/3)
##print(0.3333333333333333 * 3)
##print(1/3*3)

##print(1.1 + 2.2 - 3.3)

print('9 / 2 =', 9/2)
print('9 // 2 =', 9//2) # div, -> 9 div 2, div != division (egész számra oszt -> maradékos osztás)
print('9 % 2 =', 9%2) #mod, modulo (az osztás maradékát adja vissza)

num = 3.33333
roundedToInt = round(num)
roundedTo2decimal = round(num, 2)
print(num, 'egészre kerekítve:', roundedToInt)
print(num, 'kerekítve 2 tizedes jegyig:', roundedTo2decimal)

print('167,2 kerkítve -1 tizedes jegyig:', round(167.2, -1)) # -> 170
print('167,2 kerkítve -2 tizedes jegyig:', round(167.2, -2)) # -> 200
