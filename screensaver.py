import subprocess as sp

out = sp.check_output(["stty", "size"])
out = out.decode().rstrip().split()
rows = int(out[0])
cols = int(out[1])

print("\x1b[2J")
print("\x1b[1;1f", end="")

r = 1
while r <= rows:
    c = 1
    while c <= cols:
        print('\x1b[', r, ';', c, 'f', end='')
        print('A', end='')
        c += 1
    r += 1
