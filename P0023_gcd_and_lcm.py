#!/usr/bin/env python3

# 68 és 54 legnagyobb közös osztója:
a = 15876
b = 29484
for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        print(a, 'és', b, 'legnagyobb közös osztója: ', i)
        break

# 14 és 18 legkisebb közös többszöröse:
a = 14
b = 18
for i in range(b, a*b+1):
    if i % a == 0 and i % b == 0:
        print(a, 'és', b, 'legkisebb közös többszöröse: ', i)
        break
