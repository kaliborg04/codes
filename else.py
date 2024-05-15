while True:
    s = input("Enter string: ")
    if s == '':
        break
    if len(s) >= 5:
        print("Long")
    else:
        print("Short")