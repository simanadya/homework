# # Task 1,2,3======================================
#
# a = int(input("Введите а = "))
# b = int(input("Введите b = "))
# c = int(input("Введите c = "))
# def result(a,b,c):
#     result_1 = (a + b * c)**2
#     result_2 = a - 4 * b / c
#     result_3 = (a * b + 4)/(c - 1)
#     return result_1, result_2, result_3
# result_1, result_2, result_3 = result(a, b, c)
# print ("Result 1 is = %d" % result_1)
# print ("Result 2 is = %d" % result_2)
# print ("Result 3 is = %d" % result_3)
#
# # Task 4========================================
#
# n = int(input("Введите пятизначное число: "))
# n = str(n)
# n = [int(x) for x in n]
# odd = 0
# mult = 1
# for x in n:
#     if x%2 > 0:
#         mult *= int(x)
# print("Произведение нечётных чисел = ", mult)
#
#
#
# #Task 5=============================================
#
# d1 = (input("Введите первое число: "))
# d2 = (input("Введите второе число: "))
# my_position = 10
#
# def diff_dist(d1, d2):
#     distance1 = d1 - my_position
#     distance2 = d2 - my_position
#     if distance1 >= distance2:
#         print (d1)
#     else:
#         print (d2)
#     return diff_dist(d1,d2)
# # diff_dist(dist1).sort(key = my_position)
# # abs.sort(key = diff_dist)
# print(diff_dist(d1,d2))

#Task 7============================================

fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def listsum(fib_list):
    sum = 0
    for i in fib_list:
        sum = sum + i
    return sum

print(listsum([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))