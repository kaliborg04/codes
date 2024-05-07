N = 0
while True:
    s = input("Enter number: ")
    if len(s) == 0:
        print(N)
        exit(0)
    n = int(s)
    N += n