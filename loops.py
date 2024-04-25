# to reach the end, input:
# 1. i
# 2. hi
# 3. hello
# 4. oh my coat
# 5. ""

s = input("Введите строку: ")
while s == "hi":
    print("Hello")

f = input("Введите строку: ")
while f == "bye":
    print("goodbye")

b = input("Введите строку: ")
while b != "hello":
    print("coat")

st = input("Введите строку: ")
while st != "oh my coat":
    print("oh my coat")

coat = input("Введите строку: ")
while len(coat) >= len(s):
    print("ok")
