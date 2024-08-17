s = "hello"
print(s.upper()) # "HELLO"
print(s) # "hello"
s = s.upper()
a = [14, 34, 89, 12, 12]
a.append(0)
print(a) # [14, 34, 89, 12, 12, 0]
a.clear()
print(a) # []
a = [14, 34, 89, 12, 12, 0]
s = a.copy()
print(s) # [14, 34, 89, 12, 12, 0]
print(a.count(12)) # 2
print(a.index(0)) # 5
print(a.index(12, 2)) # 3
print(a.index(34, 0, 4)) # 1
a.insert(2, 550)
print(a) # [14, 34, 550, 89, 12, 12, 0]
print(a.pop()) # 0
print(a) # [14, 34, 550, 89, 12, 12]
x = a.pop()
print(x) # 12
a.remove(12)
print(a) # [14, 34, 550, 89]
a.reverse()
print(a) # [89, 550, 34, 14]
a.sort()
print(a) # [14, 34, 89, 550]
a.sort(reverse = True)
print(a) # [550, 89, 34, 14]
