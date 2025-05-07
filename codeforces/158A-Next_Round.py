from sys import stdin

_, k = stdin.readline().split()
k = int(k)

pts = []
for s in stdin.readline().split():
    pts.append(int(s))

pts_k = pts[k - 1]
n = 0
for p in pts:
    if p > 0 and p >= pts_k:
        n += 1
print(n)
