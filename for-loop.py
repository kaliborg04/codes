import random

for i in range(0, 10):
    print(i, random.randint(1, 99))

print()
s = input("Enter string: ")
for c in s:
    print(c)

print()
l = ["nik", "fil", "vlad"]
for name in l:
    print(name)