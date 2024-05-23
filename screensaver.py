import subprocess as sp
import random
import time

out = sp.check_output(["stty", "size"])
out = out.decode().rstrip().split()
rows = int(out[0])
cols = int(out[1])

print("\x1b[2J")
print("\x1b[1;1f", end="")

while True:
    r = 1
    while r <= rows:
        c = 1
        while c <= cols:
            print('\x1b[', r, ';', c, 'f', end='')
            color = random.randint(41, 47)
            print(f'\x1b[{color}m', end='')
            print(' ', end='')
            c += 1
        r += 1
    time.sleep(0.1)
