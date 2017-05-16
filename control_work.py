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

import math
d1 = int(input("Введите первое число: "))
d2 = int(input("Введите второе число: "))
my_position = 10
distance1 = math.fabs(int(my_position - d1))
distance2 = math.fabs(int(my_position - d2))

def diff_dist(d1, d2):
    if distance2 == distance1:
        print("Числа ", d1, " и ", d2," равноудалены от ", my_position)
    if distance1 > distance2:
        print("Число ", d2, " ближе к ", my_position)
    if distance1 < distance2:
        print("Число ", d1, " ближе к ", my_position)
    return diff_dist
print(diff_dist(d1, d2))

#Task 6=================================================

lst = [2,5,4,3,6,7,9,0,5,8]

import random


# N = 10
# a = [0,0,0,0,0,0,0,0,0,0]
# b = [0,0,0,0,0,0,0,0,0,0]
# c = [0,0,0,0,0,0,0,0,0,0]
def random_list(lst):
    # for i in range(len(list)):
        lst = []
        import random
        # for elem in enumerate(lst):
        list = [randint(lst) for i in range(n)]
        # lst = random.shuffle(lst)
        return random_list
# print("Введите числа: ")
# for i in range(len(list)):
#     b[i] = int(input())
# for i in range(len(list)):
#     c[i] = a[i] + b[i]
print(lst)
# print(b)
# print(c)

#Task 7============================================

def fib_list(n):
    d = [0, 1]
    for i in range(2, n + 1):
        d.append(d[i-1] + d[i-2])
    print(d)
n = 10
fib_list(n)

def listsum(fib_list):
    sum = 0
    for i in fib_list:
        sum = sum + i
    return sum
print("Сумма десяти первых чисел ряда Фибоначчи = ", sum)

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