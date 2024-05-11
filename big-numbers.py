nums = []
while True:
    s = input("Enter number: ")
    if len(s) == 0:
        break
    if s.isdigit():
        nums += [int(s)]

print(nums)
print("Big numbers:")
for n in nums:
    if n > 100:
        print(n)