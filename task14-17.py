# Task 14==========================================

digit = int(input("Введите число:"))

def is_even(x):
    return x%2 == 0
if is_even(digit):
    print("%d is even" % digit)
else:
    print("%d is odd" % digit)
   
# # Task 15===========================================

import math
x1 = int(input("Координaта x1:"))
y1 = int(input("Координaта y1:"))
r1 = int(input("Координата радиуса r1:"))
x2 = int(input("Координaта x2:"))
y2 = int(input("Координaта y2:"))
r2 = int(input("Координата радиуса r2:"))
result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (r2 - r1)**2)


def intersection_of_the_circles(x1, y1, r1, x2, y2, r2):
    return x1, y1, r1, x2, y2, r2 == 0
if intersection_of_the_circles(result):
    print ("%result - Intersectioned" % result)
else:
    print("%result - Not Intersectioned" % result)
    

# Task 16===================================================

v1 = 12
v2 = 70
time1 = 4/v1
time2 = 6/v2

def train_clash (v1, v2):
    return v1, v2 ==0
if time1<time2:
    print ("clash")
else:
    print("ok")

#
# Task 17========================================

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))


Discriminant = int(b**2) - int(4) * int(a) * int(c)
print("D = ", Discriminant)

def solve_equation (a, b, c ):
    if Discriminant > 0:
        D = (int(Discriminant) ** 0.5)
        x1 = (-b + Discriminant) / (2 * a)
        print("x1 = ", x1)
        x2 = (-b - Discriminant) / (2 * a)
        print("x2 = ", x2)
    elif Discriminant == 0:
        D = -b / (2 * a)
        print("x = ", Discriminant)
    else:
        print("None")

x1, x2 = solve_equation(a, b, c)
print("Equation (a=%d, b=%d, c=%d) has roots: %s, %s" % (a, b, c, x1, x2))
