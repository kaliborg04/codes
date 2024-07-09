april = [6,9,2,5]
print(april) # [6, 9, 2, 5]
s = [True, 'abvgd', [49]]
print(s) # [True, 'abvgd', [49]]
b = []
print(b) # []
print(type(b)) # <class 'list'>
print(len([2,5,8,0])) # 4
print(len(s)) # 3
print(len(b)) # 0 
print([9, 3, 1] + [8, 1, 9]) # [9, 3, 1, 8, 1, 9]
s = s + [190] # [True, 'abvgd', [49], 190]
print(s)
s = ['hi'] + s # ['hi', True, 'abvgd' [49, 190]]
print(s) 
print([9] * 9) # [9, 9, 9, 9, 9, 9, 9, 9, 9]
print(49 in s) # False
y = [1, 100,]
print(y) 
print(max(y)) # 100
print(min(y)) # -9
print(sum(y)) # 126
print(sorted(y)) # [1, 100]
print(sorted(y, reverse = True) ) # [100 , 1]
print([850] > [25, 44]) # True
print([4680] == [4680]) # True
