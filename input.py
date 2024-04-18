s = input("Введите строку: ")
print("Строка:", s)
n = len(s)
print('Длина:', n)
if n > 5:
    print("Строка длинная")
if s == "дурак":
    print("сам дурак!")
    exit(1)

print()
s = input("Введите число: ")
n = int(s)
print(n, type(n))
if n >= 10000:
    print("Число большое")
