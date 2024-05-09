f = open("wc.py")
i = 1
for s in f:
    print(i, s.rstrip('\n'))
    i += 1