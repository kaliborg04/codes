from sys import stdin

s1 = stdin.readline().upper()
s2 = stdin.readline().upper()
if s1 < s2:
    print(-1)
elif s1 > s2:
    print(1)
else:
    print(0)
