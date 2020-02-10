#!/usr/bin/env python3


numbers = [1, 100, 300, 156, 21, 212, 45, 34, 78, 107]
smallerthan100 = []
atleast100 = []

for num in numbers:
    if num < 100:
        smallerthan100.append(num)
    else:
        atleast100.append(num)


print('eredeti lista:', numbers)
print('szétválogatás után:\n100-nál kisebbek:', smallerthan100)
print('legalább 100 értékűek:', atleast100)