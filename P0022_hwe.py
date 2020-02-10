#!/usr/bin/env python3

##Hozz létre 10-30 közötti véletlenszámokból egy 30 elemű listát!
##Ez a vendéglőd elmúlt hónapjának forgalma, ennyi vendéged volt az egyes napokon.
##Ha van benne legalább egyetlen alkalommal 30 vendég, akkor rájössz,
##hogy szükséged van a vendéglő bővítésére.
##Ha van három egymás utáni nap, amikor legfeljebb 12-en voltak,
##akkor reklámozni kell. Írd ki, hogy melyik teendőt kell ellátnod!

import random


lst = []
for _ in range(0, 30):
    lst.append(random.randint(10, 30))
print(lst)
if 30 in lst:
    print('Bővíteni kell a vendéglőt!')
for i in range(2, len(lst)):
    if (lst[i-2] <= 12 and lst[i-1] <= 12 and lst[i] <= 12):
        print(i-1, '-ik naptól kezdve kevesen voltak...', sep='')
        print('Reklámozni kell a vendéglőt!')
        break
