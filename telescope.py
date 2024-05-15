bodies = {}
while True:
    body = input("Enter celestial body: ")
    if len(body) == 0:
        break
    if body not in bodies:
        bodies[body] = 1
    else:
        bodies[body] += 1
print(bodies)