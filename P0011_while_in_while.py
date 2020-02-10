#!/usr/bin/env python3

row = 0
while row < 25:
    column = 0
    while column <= row:
        print('O',end = '')
        column += 1
    print('')
    row += 1
    
