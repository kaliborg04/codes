import time

def hello(username):
    print('\x1b[2J', end='')
    print('\x1b[1;1f', end='')
    print('hello', username)
    time.sleep(1)

def goodbye(username):
    n = 4
    while n > 0:
        print('\x1b[2J', end='')
        print('\x1b[1;4f', end='')
        print(username)    
        time.sleep(0.05)
        print('\x1b[2J', end='')
        print('\x1b[1;1f', end='')
        print(username)
        time.sleep(0.05)
        n -= 1
    time.sleep(0.5)

for name in ['shane', 'tam', 'sam', 'tom']:
    hello(name)

for name in ['shane', 'tam', 'sam', 'tom']:
    goodbye(name)