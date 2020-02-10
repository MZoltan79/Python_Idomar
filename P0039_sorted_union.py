#!/usr/bin/env python3


import timeit


def sorted_union(lst1, lst2):
    return sorted(set(lst1 + lst2))


def sort_and_union(lst1, lst2):
    i, j = 0, 0
    result_list = []
    n = len(lst1)
    m = len(lst2)

    while i < n and j < m:
        if lst1[i] < lst2[j]:
            result_list.append(lst1[i])
            i += 1
        elif lst1[i] == lst2[j]:
            result_list.append(lst1[i])
            i += 1
            j += 1
        else:
            result_list.append(lst2[j])
            j += 1
    if i < n:
        result_list.extend(lst1[i:])
    if j < m:
        result_list.extend(lst2[j:])
    return result_list


evens = [0, 2, 4, 6, 8, 10, 12, 14, 14]
odds = [0, 1, 3, 5, 7, 9]

sorted_union1 = sort_and_union(evens, odds)
print(sorted_union1)
sorted_union2 = sorted_union(evens, odds)
print(sorted_union2)

evens = list(range(0, 10000000, 2))
odds = [0]
odds = list(range(1, 20000000, 2))

print(timeit.timeit('sorted_union(evens, odds)', number=5, globals=globals()))
print(timeit.timeit('sort_and_union(evens, odds)', number=5, globals=globals()))
