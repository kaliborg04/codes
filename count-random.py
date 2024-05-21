import random

nums = []
i = 0
while i < 10:
    nums.append(random.randint(-5, 5))
    i += 1
print(nums)

positive = 0
negative = 0
zeros = 0
for num in nums:
    if num > 0:
        positive += 1
    if num < 0:
        negative += 1
    if num == 0:
        zeros += 1
print("positive", positive)
print("negative", negative)
print("zeros", zeros)
