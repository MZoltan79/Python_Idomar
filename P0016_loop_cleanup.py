#!/usr/bin/env python3
#írjuk ki az 500 - 1000 közöti páros számokat, négyzetüket, köbüket, negyedik hatványukat
print('''
ciklus sz 500-tól 1000-ig 2-es lépésközzel
    ki: sz, sz^2, sz^3, sz^4
ciklus vége
''')

##for number in range(500, 1001, 2):
##    print(number, number**2, number**3, number**4)

num = 500
while num <= 1000:
     print(num, num**2, num**3, num**4)
     num += 2
