cars = {}
while True:
    car = input('Enter car: ')
    if car == '':
        break
    if car not in cars:
        cars[car] = 1
    else:
        cars[car] += 1
print(cars)
