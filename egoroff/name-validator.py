name = input("Enter name: ")
if len(name) <= 5:
    print('false')
    exit()
if not name[:5].isalpha():
    print('false')
    exit()
if not name[5:].isdigit():
    print('false')
    exit()
print('true')
