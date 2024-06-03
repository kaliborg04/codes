stars = {}
while True:
    star = input('Enter srar: ')
    if star == '':
        break
    if star not in stars:
        stars[star] = 1
    else:
        stars[star] += 1
print(stars)
