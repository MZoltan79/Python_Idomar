#!/usr/bin/env python3

# lst = ['alma', 'banán', 'cékla', 'cékla']
# lstSet = set(lst)
# print(lstSet)
# for item in lstSet:
#     print(item)
# lstSet.add('cékla')
# print(lstSet)
# lstSet.add('zeller')
# print(lstSet)
# lstSet.remove('zeller')
# print(lstSet)

set1 = {1, 2, 3, 4, 5, 4, 4}
set2 = {5, 5, 6, 7, 10, 10, 8, 9}
print('A két halmazunk:\n1.:', set1, '\n2.:', set2)

# halmazok metszete:
set_intersection = set1 & set2
print('\nmetszetük:', set_intersection)

# halmazok uniója:
set_union = set1 | set2
print('\nuniójuk:', set_union)

# halmazok különbsége:
set_difference = set1 - set2
print('\nkülönbségük:', set_difference)

# halmazok szimmetrikus differenciája:
set_symmetric_difference = set1 ^ set2
print('\nszimmetrikus differenciájuk:', set_symmetric_difference)
