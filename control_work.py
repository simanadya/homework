# Task 1,2,3======================================

a = int(input("Введите а = "))
b = int(input("Введите b = "))
c = int(input("Введите c = "))
def result(a,b,c):
    result_1 = (a + b * c)**2
    result_2 = a - 4 * b / c
    result_3 = (a * b + 4)/(c - 1)
    return result_1, result_2, result_3
result_1, result_2, result_3 = result(a, b, c)
print ("Result 1 is = %d" % result_1)
print ("Result 2 is = %d" % result_2)
print ("Result 3 is = %d" % result_3)

# Task 4========================================

n = int(input("Введите пятизначное число: "))
n = str(n)
n = [int(x) for x in n]
odd = 0
mult = 1
for x in n:
    if x%2 > 0:
        mult *= int(x)
print("Произведение нечётных чисел = ", mult)



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
# #Task 7============================================
#
# fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#
# def listsum(fib_list):
#     sum = 0
#     for i in fib_list:
#         sum = sum + i
#     return sum
#
# print("Сумма десяти первых чисел ряда Фибоначчи = ", listsum([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))

#Task 6=================================================
#
# from random import random
# N = 10
# a = [0,0,0,0,0,0,0,0,0,0]
# b = [0,0,0,0,0,0,0,0,0,0]
# c = [0,0,0,0,0,0,0,0,0,0]
# for i in range(N):
#     a[i] = int(random() * 100)
# print("Введите числа: ")
# for i in range(N):
#     b[i] = int(input())
# for i in range(N):
#     c[i] = a[i] + b[i]
# print(a)
# print(b)
# print(c)

#Task 8========================================

from random import random
N = 6
v = [0]*N
for i in range(N):
    v[i] = int(random()*100)
    print(v[i], end=' ')
print()
min = 0
max = 0
for i in range(N):
    if v[i] < v[min]:
        min = i

    elif v[i] > v[max]:
        max = i

print("Max elem = ", max)
print("Min elem = ", min)
print('v[%d]=%d v[%d]=%d' % (min+1, v[min], max+1, v[max]))
b = v[min]
v[min] = v[max]
v[max] = b

for i in range(6):
    print(v[i],end=' ')
print()