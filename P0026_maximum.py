#!/usr/bin/env python3

numbers = [1, 4, 7, 13, 3, 5, 18, 12, 19, 11, 5, 17]

maximum = 0
for num in numbers:
    if num > maximum:
        maximum = num

print('Tessék, itt a maximum:', maximum)

# max() függvénnyel jóval egyszerűbb :)
print('Ez pedig a jóval egyszerűbb megoldása:', max(numbers))


# --------  Stringek ----------
# magyar ékezetes betűkkel NEM működik!!!

names = ['Elza', 'Melinda', 'Ferenc', 'Barbara', 'Vilma', 'Miklos', 'Ambrus',\
         'Maria', 'Natalia', 'Judit', 'Arpad', 'Gabriella', 'Luca', 'Szilarda',\
         'Valer', 'Aletta', 'Lazar', 'Auguszta', 'Viola', 'Teofil', 'Tamas',\
         'Zeno', 'Viktoria', 'Adam', 'Eugenia', 'Istvan', 'Janos', 'Kamilla',\
         'Tamara', 'David', 'Szilveszter']

print(min(names)) # ABC eleje...
print(max(names)) # ABC vége...
