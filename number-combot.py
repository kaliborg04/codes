import random

number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number1 = random.randint(1, 9)
number2 = random.randint(1, 9)
print(number1, 'vs', number2)
if number1 > number2:
    print('good job')
if number1 < number2:
    print('no')
if number1 == number2:
    print('good')
