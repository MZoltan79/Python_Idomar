#!/usr/bin/env python3

def name(name):
    return name.split()[1]


# nums = [5, 3, 9, 1, 7]
# print(nums)

names = ['Dorogi Zsiga', 'Molnár Bálint', 'Aba Samu', 'Batyú Ferenc']

print(names)

# buborék rendezés implementálva:

# for i in range(len(nums)-1, 1, -1):
#	unchanged = True
#	for j in range(0, i):
#		if(nums[j] > nums[j+1]):
#			nums[j], nums[j+1] = nums[j+1], nums[j]
#			unchanged = False
#	if  unchanged:
#		break

# beépített rendezö tagfüggvénye a list-nek:

# nums.sort()
# nums.sort(reverse = True)

# numsSorted = sorted(nums) # ez nem bántja az eredeti listát, 
# hanem annak rendezett példányával tér vissza
# print(numsSorted)

names.sort(reverse=True, key=name)
# a sort()  és a sorted() függvényeknél egyaránt paraméterezhetö,
# a reverse = True\False, és a key = "metódus"
print(names)

# print(nums)
