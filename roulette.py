import random

names = ['nik', 'fil', 'vlad', 'petya', 'sam', 'vova']
i = random.randint(0, len(names) - 1)
name = names[i]
print("Player:", name)

cash = random.randint(100, 1000)
print('Cash:', cash)

rounds = int(input('Enter rounds: '))
nround = 1
while nround <= rounds: 
    print('*' * 10)
    n = random.randint(1, 5)
    bet = cash // n
    print('Bet:', bet)
    
    win = random.randint(0, 1)
    if win == 1:
        cash += bet
        print('Bet wins')
    else:
        cash -= bet
        print('Bet does not win')
    print('Cash:', cash)
    if cash <= 0:
        break

    nround += 1
