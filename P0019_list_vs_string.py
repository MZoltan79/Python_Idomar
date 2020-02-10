#!/usr/bin/env python3

str1 = 'farmotoros'
str2 = 'hegyi-kecskék'

list1 = ['ez', 'jó', 'rég', 'volt...']
list2 =['alig', 'emlékszem', 'rá.']
print('eredeti stringek:')
print('str1 és str2: ', str1, ', ',str2)

# mind2 indexelhető, szeletelhető, egyelhető, számolható az elemei/karakterei száma (count),
# illetve a lista/string hossza (len)

print('\n', str2, ' stringben a k betűk száma: ', str2.count('k'), sep = '')
print(list1, ' listában a "jó" előfordulása(i): ', list1.count('jó'), sep = '')

print('\nstr2: ', str2, ' hossza ', len(str2), ' karakter.', sep = '')
print('list1: ', list1, ' hossza ', len(list1), ' elem.', sep = '')


print('\nindexelve:\nstring karakterei:')
print(str1[3], str2[-2])

print('\nlista elemei: ')
print(list1[0], list1[-2])

print('\nszeletelve:\nstring szeletelve:')
print(str1[1:], str2[2:])

print('\nlista szeletelve:')
print(list1[1:3])

print('\negyelve:\nstring egyelve:')
print(str1[::2], str2[-1::-2])
print(str1[::-1], str2[::-1])

print('\nlista egyelve:')
print(list1[1:4:2])
print(list2[::-1])

# append, extend , insert tagfüggvények
print('\nappend, extend, insert, remove és pop függvények listánál működnek stringnél nem!\n')
text1 = 'Mici'
text2 = 'Mackó'

tmpList1 = ['Üdvözöllek', 'dicső', 'lovag']
tmpList2 = ['Szép', 'a', 'ruhád', 'szép', 'a', 'lovad']

##tmpList2.append('is')
##print(tmpList2)

# ---- NEM MEGY ----
##text2.append('!')
##text2.extend(text1)
##print(text2)


##tmpList2.insert(3, 'bizonyám')
##print(tmpList2)

# ---- NEM MEGY ----
##text2.insert(3, '!')

##tmpList2.remove('a')
##print(tmpList2)

# ---- NEM MEGY ----
##text2.remove('a')
##print(text2)

##tmpList2.pop()
##print(tmpList2)

# ---- NEM MEGY ----
##text2.pop()
##print(text2)
