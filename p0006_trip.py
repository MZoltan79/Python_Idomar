#!/usr/bin/env python3

season = input('What season is it? (summer/fall) ')
rains = input('Is it raining? (y/n) ')
wind = input('Is it windy out there? (y/n) ')

##if (season == 'summer' and wind == 'n') or (season == 'fall' and rains == 'n' and wind == 'n'):
if wind == 'n' and (season == 'summer' or (season == 'fall' and rains == 'n')):
    print('Let\'s go!')
else:
    print('Okay, it\'s cold out there, thus we stay at home.\nLet\'s code!')
