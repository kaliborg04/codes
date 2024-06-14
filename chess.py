import random

chess = [1, 2, 3, 4, 5]
chess = random.randint(0, 4)
n1player = random.randint(0, 4)
vs = 'vs'
n2player = random.randint(0, 4)
print(n1player, vs, n2player)
wins = input('Enter wins:')
if n2player == n1player:
    n2player += 2
sinsey = input('GOOD')
if n2player == 3:
    print('WHAT')
if n1player == 3:
    print('WHAT')


