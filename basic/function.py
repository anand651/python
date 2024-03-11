# def greet():
#     print("hi")
#     print("good morning")
#
# greet()
# greet()
'''hi
good morning
hi
good morning'''

import math

# def greet(name):
#     print(f"hii {name}")
#     print("are you cs departement")
#
# greet("anand")
'''hii anand
are you cs departement'''

# def add(a,b):
#     c=a+b
#     print(f"sum is {c}")
#
# add(5,7)
'''sum is 12'''

'''types of arguments 
 default
 positional
 keyword
 arbitrary / varible length
    arbitrary positional
    arbitrary keyword'''

'''positional argument'''
# def greet(name,dept):
#     print(f"hi {name}")
#     print(f"are you from {dept} department")
#
# greet("jenny","cs")

'''hi jenny
are you from cs department'''

'''keyword argument'''
# def greet(name,dept):
#     print(f"hi {name}")
#     print(f"are you from {dept} department")
#
# greet(name="jenny", dept="cs")
# greet(dept="cs",name="jenny")
# greet("jenny",dept="cs")      #positional argument+keyword argument
# # greet(dept="cs","jenny")          #error

'''hi jenny
are you from cs department
hi jenny
are you from cs department
hi jenny
are you from cs department'''

# def greet(name,dept="cs"):
#     print(f"hi {name}")
#     print(f"are you from {dept} department")
#
# greet("jenny","it")
# greet("anand")
'''hi jenny
are you from it department
hi anand
are you from cs department'''

''' arbitrary positional'''
# def add(*number):
#     c=0
#     for i in number:
#         c=c+i
#     print(f"sum is {c}")
#
# add(1,2,3,4,5,6)
# add(5,9,7,8)
'''sum is 21
sum is 29'''

# def add(*number):   #(1,2,3,4,5,6)
#     c=0
#     print(number[0])
#     number[0]=4              #error
#     for i in number:
#         c=c+i
#     print(f"sum is {c}")
#
# add(1,2)

# def add(*number,name):   #(1,2,3,4,5,6)
#     c=0
#     print(name)
#     for i in number:
#         c=c+i
#     print(f"sum is {c}")
#
# add(1,2,"jenny")                       #error

# def add(*number,name):   #(1,2,3,4,5,6)
#     c=0
#     print(name)
#     for i in number:
#         c=c+i
#     print(f"sum is {c}")
#
# add(1,2,name="jenny")

'''jenny
sum is 3'''

# def add(a,*number):
#     c=0
#     print(a)
#     print(number)
#     for i in number:
#         c+=i
#     print(f"sum is {c}")
# add(5,1,2)
'''5
(1, 2)
sum is 3'''

# def multi(*num):
#     c=1
#     for i in num:
#         c*=i
#     print(f"multiply of {c}")
#
# multi(2,3,-6,8)
# multi(2,5,8,9,6)
'''multiply of -288
multiply of 4320'''


'''arbitrary keyword'''
# def info_person(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)
# info_person(name="jenny",age=30,dept="cse")
# info_person(name="shyam",dept="pcm")
'''name jenny
age 30
dept cse
name shyam
dept pcm'''

# def info_person(*arg,**kwargs):
#     for key,value in kwargs.items():
#         print(arg,key,value)
# info_person(name="jenny",age=30,dept="cse")
# info_person(1,2,3,name="shyam",dept="pcm")
'''() name jenny
() age 30
() dept cse
(1, 2, 3) name shyam
(1, 2, 3) dept pcm'''

# height = int(input("height of the wall"))
# width = int(input("width of wall"))
# can = int(input("how much wall can be painted by the 1 can"))
# no_of_can = (height*width)/can
# print(math.ceil(no_of_can))
'''height of the wall7
width of wall7
how much wall can be painted by the 1 can5
10'''

# import math
# def paint_calculation(height,width,cover):
#     area = height*width
#     no_of_can = math.ceil(area/cover)
#     print(f"you will need {no_of_can} can of paint")
# h = int(input("height of the wall"))
# w = int(input("width of wall"))
# coverage = 7
# paint_calculation(width=w,height=h,cover=coverage)
'''height of the wall3
width of wall4
you will need 2 can of paint'''

# def prime(number):
#     i=2
#     while i<number:
#         if number%i ==0:
#             print(f"{number} is not a prime number")
#             i=i+1
#             break
#         else:
#             i=i+1
#     if i==number:
#         print(f"{number} is prime")
#
# p=int(input("enter a number"))
# prime(number=p)
'''enter a number11
11 is prime'''

# def prime_checker(number):
#     is_prime = True
#     if number ==1:
#         is_prime=False
#     for i in range(2,number):
#         if number%i == 0:
#             is_prime = False
#     if is_prime ==True:
#         print("it ia a prime number")
#     else:
#         print("it is not a prime number")
# n=int(input("enter a number:\n"))
# prime_checker(n)
'''enter a number:
89
it ia a prime number'''

import math
# def prime_checker(number):
#     is_prime = True
#     if number ==1:
#         is_prime=False
#     for i in range(2,math.ceil(number/2)+1):
#         if number%i == 0:
#             is_prime = False
#     if is_prime ==True:
#         print("it ia a prime number")
#     else:
#         print("it is not a prime number")
# n=int(input("enter a number:\n"))
# prime_checker(n)

'''enter a number:
34
it is not a prime number'''

# a=int(input("enter a number"))
# print(math.ceil(math.sqrt(a)))
'''enter a number16
4'''

# import math
# def prime_checker(number):
#     is_prime = True
#     if number ==1:
#         is_prime=False
#     for i in range(2,math.ceil(math.sqrt(number))):
#         if number%i == 0:
#             is_prime = False
#     if is_prime ==True:
#         print("it ia a prime number")
#     else:
#         print("it is not a prime number")
# n=int(input("enter a number:\n"))
# prime_checker(n)
'''enter a number:
9
it ia a prime number'''

