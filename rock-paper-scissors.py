import random

names = ['nik', 'petya', 'vlad', 'fil', 'sam', 'oleg']
i = random.randint(0, 5)
p1name = names[i]
i = random.randint(0, 5)
p2name = names[i]
print(p1name, 'vs', p2name)

wins = {}
wins[p1name] = 0
wins[p2name] = 0

rounds = int(input('Enter rounds: '))
nround = 1
while nround <= rounds:
    nround += 1
    n = random.randint(1, 2)
    if n == 1:
        wins[p1name] += 1
        print(p1name, 'wins')
    else:
        wins[p2name] += 1
        print(p2name, 'wins')
print(wins)
