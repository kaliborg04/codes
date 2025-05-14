from sys import stdin

nums = [int(s) for s in stdin.readline().split('+')]
nums.sort()
print('+'.join([str(n) for n in nums]))
