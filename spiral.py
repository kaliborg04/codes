from turtle import *

speed(10)
dist = 5 
step = float(input("Шаг дистанции: "))
alpha = float(input("Угол поворота: "))
n = 500
for i in range(n):
    print(i)
    fd(dist)
    rt(alpha)
    dist += step
input()
