import random

secret = random.randint(1, 100)
while True:
    s = input("Enter number from 1 to 100: ")
    if len(s) == 0:
        break

    n = int(s)
    if n == secret:
        print("Good job!")
        break

    if secret > n:
        print("Secret is bigger")

    if secret < n:
        print("Secret is smaller")