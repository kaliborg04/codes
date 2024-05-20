print('\x1b[2J', end='')
print('\x1b[1;1f', end='')

cities = {}
while True:
    s = input("Enter city: ")
    s = s.lower().replace("-", " ")

    n = input("Enter name: ")
    if len(n) == 0:
        print(n)
        break
    n = n.lower()
    n = n.replace(",", " ").replace("-", " ")
    print(s, n)

    if s not in cities:
        cities[s] = [n]
    else:
        cities[s] += [n]
print(cities)