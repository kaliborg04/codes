import sys

sys.stdin.readline()
x = 0
for line in sys.stdin:
    line = line.rstrip()
    if line == '--X' or line == 'X--':
        x -= 1
    elif line == '++X' or line == 'X++':
        x += 1
    else:
        assert 0
print(x)
