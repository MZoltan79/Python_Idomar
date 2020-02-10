#!/usr/bin/env python3

x = 0
counter = 1
print('3x + 4y = 52 összes megoldása a természetes számok halmazán:\n')
while 3*x <= 52:
    y = 0
    while 4*y <= 52:
        if (3 * x + 4 * y) == 52:
            print(counter, '. megoldás: x = ', x, ' és y = ', y, sep='')
            counter += 1
        y += 1
    x += 1

