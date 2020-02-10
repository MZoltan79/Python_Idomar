#!/usr/bin/env python3

number = 4
guessed = False
limit = 0

while not guessed and limit < 3:
    guess = int(input('Guess a number in range 1 - 5! '))
    if guess == number:
        guessed = True
    limit += 1
print('Bye!')
