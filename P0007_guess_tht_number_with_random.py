#!/usr/bin/env python3

import random

LOWER_BOUND = 1
UPPER_BOUND = 4

number = random.randint(LOWER_BOUND, UPPER_BOUND)
guessed = False
limit = 0

while not guessed and limit < 3:
    guess = int(input('Guess a number in range ' + str(LOWER_BOUND) + ' - ' + str(UPPER_BOUND) + '! '))
    if guess == number:
        guessed = True
    limit += 1
if guessed:
    print('Congrats!\nBye!')
else:
    print('Bad luck...\nBye!')
