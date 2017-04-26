# lst = [1,2,3,4,5]
# print(lst)
# #
# s = "abc"
# for c in s:
#     print (c)
#     print("elem", c)
#
# # for elem in lst:        /распечатать элементы списка
# #     print (elem)
# #
# for i, elem in enumerate (lst):    #/знание индекса
#     print (i, elem)
#     lst[i] = elem**2
#
# for i in range (len(lst)):        #кенерируем индексы и потом оперируем ими
#     # можем устанавливать шаг In range (o, len (lst),3)
#     print(lst[i])
#     lst[i] = lst[i] ** 3

#
# # # lst[0] = lst[0]**2
# # print (lst)

# ===============
# s = [45,56,33]
# print(s)
#
# for elem in s:
#     print (elem)
#
# for i, elem in enumerate(s):
#     print(i, elem)
#     s[i] = elem**3
#
# print(s)

# =============

# def create_random_list(num, lower_limit, upper_limit):
#     import random
#     lst = []
#     for i in range(num):
#         lst.append(random.randint(lower_limit, upper_limit))
#     return lst
#
# def print_list(lst):
#     for elem in lst:
#         print("Element of the list is equal to", elem)
#
# def print_list_2(lst):
#     for i, elem in enumerate(lst):
#         print("%dth element of the list is equal to %d" % (i, elem))
#
# def print_list_3(lst):
#     for i in range(len(lst)):
#         print("%dth element of the list is equal to %d" % (i, lst[i]))
#
# def max_list_elem(lst):
#     max_elem = lst[0]
#     for elem in lst:
#         # max определяем текущий макс
#         if elem > max_elem:
#             max_elem = elem
#     return max_elem
#
# def square_list(lst):  #возведенеие элементов в квадрат
#     for i, elem in enumerate(lst):
#         lst[i] = elem ** 2
#
# def square_list_2(lst):
#     for i in range(len(lst)):
#         lst[i] = lst[i] ** 2
#
# lst = create_random_list(10, 0, 100)
# print_list_2(lst)
# square_list(lst)
# print_list_2(lst)

# # print("Max:", max_list_elem(lst))
#
#
# #min
#
#
# def min_random_list(num, lower_limit, upper_limit):
#     import random
#     lst = []
#     for i in range(num):
#         lst.append(random.randint(lower_limit, upper_limit))
#     return lst
#
# def print_list(lst):
#     for elem in lst:
#         print("Element of the list is equal to", elem)
#
# def min_list_elem(lst):
#     min_elem = lst[0]
#     for elem in lst:
#             # min определяем текущий
#         if elem < min_elem:
#             min_elem = elem
#     return min_elem
#
#
# lst = min_random_list(10, 0, 100)
# print_list(lst)
#
# print("Min:", min_list_elem(lst))
#
# #normalize list of planets: planets = [' mercury', ' mars', ' earth', ' venus']


print("*******************************************")
#sum

sum_list_elem = [3,5,7,0,6,56]
def sum_list_elem(lst):
    import random
    total_sum = 0
    for elem in lst:   #организация элементов цикла и на каждой иттерации выводится элемент
        total_sum += elem
    return total_sum

def print_list(lst):
    for elem in lst:
        print("Element of the list is equal to", elem)


total_sum2 = sum_list_elem([3,5,7,0,6,56])
#
# print_list(lst)
# total_sum = sum(lst)


print("Sum:", total_sum2)