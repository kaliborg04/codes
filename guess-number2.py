import random

secret = random.randint(1, 100)
print("Угадай число от 1 до 100")
while True:
    s = input("Введите число: ")
    if s == "":
        print("Пока!")
        break

    n = int(s)
    if n > 100 or n < 1:
        print("От 1 до 100, дебил!!!")
        continue

    if n == secret:
        print("Угадал!")
        break

    if secret < n:
        print("Число меньше")
    if secret > n:
        print("Число больше")
