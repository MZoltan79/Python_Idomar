#!/usr/bin/env python3

print('''Numbers printed from 1 to 100.\nIf the number is divisible by 3, "Fizz" will be printed.\nIf it is divisible by 5 "Buzz" will be printed.
If it is divisible by both "FizzBuzz will be printed.\n\nTo continue, hit ENTER!"''')
cont = input()

if cont == '':
    for i in range(100):
        if ((i+1) % 3 == 0 and (i+1) % 5 == 0):
            print('FizzBuzz')
        elif (i+1) % 5 == 0:
            print('Buzz')
        elif ((i+1) % 3 == 0):
            print('Fizz')
        else:
            print(i+1)
