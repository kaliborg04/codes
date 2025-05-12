from sys import stdin

name = stdin.readline().rstrip()
letters = set()
for l in name:
    letters.add(l)
if len(letters) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
