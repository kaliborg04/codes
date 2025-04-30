import sys

n = 0
sys.stdin.readline()
for line in sys.stdin:
    line = line.rstrip()
    #print(line)
    digits = line.split()
    ones = 0
    for x in digits:
        if x == '1':
            ones += 1
    if ones >= 2:
        n += 1
print(n)
