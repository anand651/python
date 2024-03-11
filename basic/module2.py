# import module1
# print(module1.a)
# print(module1.area_of_square(7))
'''10
49'''

# import module1 as m
# print(m.a)
# print(m.area_of_square(4))
'''10
16'''

# from module1 import calculator
# calculator(3,2)
'''addition is  5
substraction is  1
multiplication is  6
division is  1.5'''

# from module1 import a,calculator
# print(a)
# calculator(8,9)
# # print(area_of_square(5))            #error
'''10
addition is  17
substraction is  -1
multiplication is  72
division is  0.8888888888888888'''

# from module1 import *
# print(a)
# print(area_of_square(3))
# calculator(3,8)
'''10
9
addition is  11
substraction is  -5
multiplication is  24
division is  0.375'''

# from module1 import a
# a,b=4,5
# sum=a+b
# print("sum is ",sum)
# print("value of a from another module is : ",a)
'''sum is  9
value of a from another module is :  4'''

import module1
a,b=4,5
sum=a+b
print("sum is ",sum)
print("value of a from another module is : ",module1.a)
'''sum is  9
value of a from another module is :  10'''