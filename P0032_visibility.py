#!/usr/bin/env python3


def method(x):
    print('bent: x =', x, 'id:', id(x))
    x = 2
    print('bent: új x =', x, 'id:', id(x))


def method2():
    print('method2(): x=', x, 'id:', id(x))  # elérjük a globális változót
    # x = 6  # ez viszont már nem fut le, mivel "x"-re egy
# sorral feljebb már hivatkoztunk, ami ugye globális, ezért innen
# nem módosíthatjuk.

def method3(lst):
    lst[0] = 'ez változott'
    lst.append('Ez meg hozzáadódott')
    print('lista id: ', id(lst), 'tartalma: ', lst)


x = 5
print('kint: x =', x, 'id:', id(x))
method(x)
print('kint: x =', x, 'id:', id(x))
method2()
lst = [1, 2]
print('lista id: ', id(lst), 'tartalma: ', lst)
# A 3-as methodban viszont változtatható a lista tartalma!!!
method3(lst)
