#!/usr/bin/env python3

numbers = [1, 5, 67, 23, 433, 64, 43, 32, 49, 54, 545]

print('A lista elemei:', numbers)

##is64 = False

##for number in numbers:
##    if number == 64:
##        is64 = True
##        break


##i = 0
##while i <  len(numbers) and not is64:
##    if numbers[i] == 64:
##        is64 = True
##    i += 1
##
##
##if is64:
##    print('Van 64 a listában')
##else:
##    print('Nincs 64 a listában')

#-----------------------------------------------------------------
##for number in numbers:
##    if number == 63:
##        print('Van ám!')
##        break
##else:
##    print("Nem volt benne!")
    
# python egyik speciális else ág funkciója for ciklushoz:
# Amennyiben a ciklus végigfut anélkül, hogy kilépne, ELSE ágra lép,
# és végrehajtja azt.
#------------------------------------------------------------------

# Végezetül egy igazán python-os megoldás:

if 64 in numbers:
    print('Van 64 a listában.')
else:
    print('Nincs 64 a listában.')


# Van-e páros szám a listában?
for number in numbers:
    if number % 2 == 0:
        print('Van köztük páros!')
        break
else:
    print("Mind páratlan!")

