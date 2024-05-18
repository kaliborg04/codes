objects = ['man', 'robot', 'dog']
actions = ['runs', 'flies', 'kills', 'dies']
for o in objects:
    for a in actions:
        print(o, a)

print()
offices = [
    ['john', 'sam'],
    ['tom', 'tony', 'petya', 'isaak'],
    ['martha', 'helen', 'tatyana'],
]
for o in offices:
    print(str(len(o)) + ': ', end='')
    for p in o:
        print(p, end=' ')
    print()