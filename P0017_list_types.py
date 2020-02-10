#!/usr/bin/env python3

myCars = ['Dacia', 'Jeep', 'Opel', 'Lotus', 'Volvo', \
            'Fiat', 'Aston Martin', 'Mazda', 'Saab', 'Toyota', 'Audi']
myNewCars = []

newCar = None
while newCar != '':
    newCar = input('Milyen autót vettél ma? ')
    if newCar != '':
        myNewCars.append(newCar)

print('Új autóim:', myNewCars)
myCars.extend(myNewCars)
print('Az összes autóm:', myCars)

carToSell = input('Mit akarsz eladni? ')
myCars.remove(carToSell)
print('Autóim eladás után: ', myCars)
print(carToSell, '-ból maradt: ', myCars.count(carToSell), ' db.', sep='')
