print ("Task 8============================================")
# task 8
#       01234567
str1 = "AAAaaAAA"
str2 = "BBBbbBBB"
in_str2 = str2[:int(len(str2)/2)] + str1 + str2[int(len(str2) / 2):]
print(in_str2)
in_str1 = str1[:int(len(str1)/2)] + in_str2 + str1[int(len(str1) / 2):]
print(in_str1)

print ("Task 9============================================")
# task 9
str1 = "abc def ghj"
idx1 = str1.find(' ')
idx2 = idx1 + str1[idx1+1:].find(' ') + 1
str2 = str1[idx1+1:idx2]
result = str1[:idx1+1] + str2.upper() + str1[idx2:]
print(result)

print ("Task 10============================================")
# task 10
str = "Leo Tolstoy*1828-08-28*1910-11-20"
idx1 = str.find('*')
idx2 = str.find('-')
birth_year = str [idx1 + 1 : idx2]
idx3 = str.find('*', idx1 + 1)
idx4 = str.find('-', idx3)
death_year = str[idx3 +1 : idx4]
name = '"' + str[:idx1] + '",'
years_old = int(death_year) - int(birth_year)
print (name, years_old)

print ("Task 11============================================")
# task 11
import math
def degrees_to_radians (dtr):
    rtd = dtr * math.pi / 180
    return rtd
print ("Cos 60 =", math.cos(degrees_to_radians(60)))
print ("Cos 45 =", math.cos(degrees_to_radians(45)))
print ("Cos 40 =", math.cos(degrees_to_radians(40)))
