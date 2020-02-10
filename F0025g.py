#!/usr/bin/env python3

# Dobj fel egy kockát 100000-szer, a dobásokat tárold listában!
# Hányszor sikerült kidobnod az egyes számokat?Az eredményeket tárold listában!

import random

randomNumbers = []

freqvencies = [0]*6

for _ in range(100000):
    randomNumbers.append(random.randint(1,6))
for num in randomNumbers:
    freqvencies[num-1] += 1

print(freqvencies)
