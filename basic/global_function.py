# a=10
# def display():
#     a=a+1
#     print(a)
# display()
'''error'''

# a=10
# def display():
#     global a
#     a=a+1
#     print(a)
# display()
'''11'''

# def display():
#     a=20
#     def show():
#          global a
#          a=a+1
#          print(a)
#     show()
# display()
'''error'''

# def display():
#     a=20
#     def show():
#         global a
#         a=30
#     print(f"value of a before calling show() function is {a}")
#     show()
#     print(f"value of a after calling show() function is {a}")
# display()
# print(a)

'''value of a before calling show() function is 20
value of a after calling show() function is 20
30'''

name="jenny's"
def display():
    global name
    name=name +" lectures"
print(name)
display()
print(name)

'''jenny's
jenny's lectures'''