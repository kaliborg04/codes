numbers = [] 
strings = []
i = 6
while i > 0:
    n = int(input('Enter number: '))
    s = input('Enter string: ')
    if n == 0:
        break
    if s == '':
        break
    i -= 1
    numbers.append(n)
    strings.append(s)
print('GOOD', numbers, strings)
