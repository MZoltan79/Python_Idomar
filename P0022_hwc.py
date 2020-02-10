#!/usr/bin/env python3

# Prímnek nevezzük azokat a természetes számokat, amelyeknek pontosan
# két osztójuk van a természetes számok között (maga a szám és az 1).
#                           - wikipedia -

number = int(input('Adj meg egy természetes számot, megmondom prím-e! '))

i = 1
while i*i < number:
    i += 1
    if number % i == 0:
        print(number, '- Nem prím.')
        break
else:
    print(number, '- Prím.')
print('Program vége!')
