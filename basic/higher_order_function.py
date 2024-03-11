# def greet():
#     print("hi")
# def display(other_def_func):
#     print("this is display() function")
# display(greet)
'''this is display() function'''

# def greet():
#     print("hi")
# def display(other_def_func):
#     print("this is display() function")
#     other_def_func()
# display(greet)
'''this is display() function
hi'''

# def greet_louder(name):
#     print(f"hi {name.upper()}")
# def greet_softer(name):
#     print(f"hi {name.lower()}")
# def hello(other_def_func,name1):
#     print("this is display() function")
#     other_def_func(name1)
#
# hello(greet_louder,"jenny")
# hello(greet_softer,"JENNY")
'''this is display() function
hi JENNY
this is display() function
hi jenny'''

# def add(a,b):
#     return a+b
# addition=add
# print(addition(3,4))
'''7'''

# def hello(name):
#     print("hello has been executed")
#     def greet():
#         print("hare krishna")
#     def welcome():
#         print("jai shree ram")
#     if name=="jenny":
#         return greet
#     else:
#         return welcome
#
# hello("jenny")
'''hello has been executed'''

# def hello(name):
#     print("hello has been executed")
#     def greet():
#         print("hare krishna")
#     def welcome():
#         print("jai shree ram")
#     if name=="jenny":
#         return greet              # without parenthesis()
#     else:
#         return welcome            # without parenthesis()
#
# new_fun=hello("jenny")
# new_fun()
'''hello has been executed
hare krishna'''

# def add(x,y):
#     print("hi")
#     return x+y
# def sub(x,y):
#     return x-y
# def mul(x,y):
#     return x*y
# def div(x,y):
#     return x/y
#
# def calculator(fun,a,b):
#     print("this is your output")
#     print(fun(a,b))
# calculator(add,5,7)
'''this is your output
hi
12'''