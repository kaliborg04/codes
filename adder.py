numbers = []
while True:
    s = input("Enter number: ")
    if len(s) == 0:
        break
    if s.isdigit():
        numbers.append(int(s))
    else:
        print("Not a number!")
print(numbers)

out = 0
for num in numbers:
    out += num
print(out)
