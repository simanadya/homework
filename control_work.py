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
#============
def result(n):
    even = 0
    odd = 0
    for x in n:
        if x%2 ==0:
            even +=1
        else:
            odd +=1
    mult *= odd(n)
    return mult
mult = result(n)
print("Произведение нечётных чисел = ", mult)
#============
def is_odd_digits(n):
    n1 = n//10000
    n2 = n//1000
    n3 = n//100
    n4 = n//10
    n5 = n//1

    if is_odd_digits(n1,n2,n3,n4,n5):
        return n % 2 != 0
        mult = n1*n2*n3*n4*n5
    else:

mult = is_odd_digits(n)
print ("Result is = %d" % mult)


#Task 5=============================================

dist1 = [float(input("Введите первое число: "))]
dist2 = [float(input("Введите второе число: "))]
my_position = 10

def diff_dist(elem):
    return abs(elem - my_position)
dist1.sort(key = diff_dist)
dist2.sort(key = diff_dist)
print (diff_dist(my_position))