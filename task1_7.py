import math

print ("Task 1============================================")
# task 1
a1 = 3
b1 = 6
c1 = 8
result1 = a1 + b1 *(c1 / 2)
print ("The result of the expression for random values :", result1)

print ("Task 2============================================")
# task 2
a2 = 2
b2 = 3
result2 = (a2**2 + b2**2) % 2
print("The result of the expression for random values :", result2)

print ("Task 3============================================")
# task 3
a3 = 50
b3 = 78
c3 = 100
result3 = (a3 + b3) / 12 * c3 %4 + b3
print ("The result of the expression for random values :", result3)

print ("Task 4============================================")
# task 4
a4 = 4
b4 = 7
c4 = 9
result4 = (a4 - b4 * c4) / (a4 + b4) %c4
print ("The result of the expression for random values :", result4)

print ("Task 5============================================")
# task 5
a5 = 25
b5 = 10
c5 = 1
result5 = math.fabs(a5 - b5) / (a5 + b5)**3 - math.cos(c5)
print ("The result of the expression for random values :", result5)

print ("Task 6============================================")
# task 6
a6 = 6
b6 = 9
c6 = 18
result6 = (math.log(1 + c6) / (-b6))**4 + math.fabs(a6)
print ("The result of the expression for random values :", result6)

print ("Task 7============================================")
# task7
#                0123456789
american_time = "05.17.2016"
idx1 = american_time.find ('.')
month = american_time[:idx1 + 1]
idx2 = american_time.find ('.', idx1 + 1)
day = american_time[idx1 +1 : idx2 + 1]
year = american_time [idx2 + 1:]
european_time = day + month + year
print (european_time)

