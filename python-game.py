s = input("Enter city: ")
print('\x1b[2J')
while True:
    n = input("Enter name: ")
    if len(n) == 0:
        print(n)
        break
    n.lower()
    n.replace(",", " ").replace("-", " ")
    print(s, n)

