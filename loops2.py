s = input("Enter string: ")
while len(s) != 0:
    print(s, len(s))
    s = input("Enter string: ")

while True:
    s = input("Enter number: ")
    n = int(s)
    if n > 100:
        break
