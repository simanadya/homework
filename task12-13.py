# Task 12===============================================

number = input("Введите трёхзначное число:")
number = int (number)

n1 = number%10
number = number//10
n2 = number%10
number = number//10
n3 = number%10

print ("Сумма цифр числа :", n1+n2+n3)


# Task 12(другой вариант)================================

n = int (input("Введите трёхзначное число:"))
def separete_digits(n):
    n1 = n//100
    n2 = n//10
    n2 = n2%10
    n3 = n%10
    sum_digits = n1 + n2 +n3
    return sum_digits
sum_digits = separete_digits(n)
print ("Сумма цифр числа =", str(sum_digits))


# Task 13================================================

a = int(input("Введите длину катета a:"))
b = int(input("Введите длину катета b:"))


def square_and_perimetr_of_triangle (a,b):
    import math
    c = math.sqrt(a ** 2 + b ** 2)
    s = (a * b)/2
    p = a + b + c
    return s, p
s, p = square_and_perimetr_of_triangle(a,b)
print ("Площадь треугольника = ", s)
print ("Периметр тругольника = ", p)
