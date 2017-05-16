#Task 5=============================================

d1 = int(input("Введите первое число: "))
d2 = int(input("Введите второе число: "))
my_position = 10
distance1 = int(my_position - d1)
distance2 = int(my_position - d2)

# def diff_dist(d1, d2):
for d1, d2 in range (distance1, distance1):
    if distance2 == distance1:
        print ("Числа ", d1," и ", d2," равноудалены от ", my_position)
    if distance1 > distance2:
        print ("Число ", d2, " ближе к ", my_position)
    if distance1 < distance2:
        print ("Число ", d1, " ближе к ", my_position)
    # return diff_dist(distance1, distance2)
# diff_dist(dist1).sort(key = my_position)
# abs.sort(key = diff_dist)
# print(diff_dist(d1, d2))
print()

#Task 6=================================================

from random import random
N = 10
a = [0,0,0,0,0,0,0,0,0,0]
b = [0,0,0,0,0,0,0,0,0,0]
c = [0,0,0,0,0,0,0,0,0,0]
for i in range(N):
    a[i] = int(random() * 100)
print("Введите числа: ")
for i in range(N):
    b[i] = int(input())
for i in range(N):
    c[i] = a[i] + b[i]
print(a)
print(b)
print(c)
