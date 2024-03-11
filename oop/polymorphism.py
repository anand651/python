''' ********************* duck typing method **********************'''

# class duck:
#     def swim(self):
#         print("i ama duck and i can also swim")
#     def speak(self):
#         print("quack quack")
# class dog:
#     def swim(self):
#         print("i ama a dog and i can swim")
#     def speak(self):
#         print("woof woof")
# class person:
#     def speak(self):
#         print("blah blah blah")
#
# def display(obj):
#     obj.swim()
#     obj.speak()
#     print("information displayed")
#
# d=duck()
# display(d)
# do=dog()
# display(do)
# per=person()
# display(per)

'''i ama duck and i can also swim
quack quack
information displayed
i ama a dog and i can swim
woof woof
information displayed
AttributeError: 'person' object has no attribute 'swim'
'''

# class duck:
#     def swim(self):
#         print("i ama duck and i can also swim")
#     def speak(self):
#         print("quack quack")
# class dog:
#     def swim(self):
#         print("i ama a dog and i can swim")
#     def speak(self):
#         print("woof woof")
# class person:
#     def speak(self):
#         print("blah blah blah")
# class demo:
#     def display(self,obj):
#         obj.swim()
#         obj.speak()
#         print("information displayed")
# d=duck()
# do=dog()
# p=person()
# dm=demo()
# dm.display(d)
# dm.display(do)
'''i ama duck and i can also swim
quack quack
information displayed
i ama a dog and i can swim
woof woof
information displayed'''


'''****************** operator overloading ******************************'''

# print(1+2)
# print("1"+"2")
# print(int.__add__(2,8))
# print(str.__add__("2","8"))

# class complexnumber:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self, other):
#        return f"{self.real + other.real} + {self.imaginary + other.imaginary}i"
# c1=complexnumber(1,3)
# c2=complexnumber(7,8)
# print(c1+c2)
'''8 + 11i '''


# class complexnumber:
#     def __init__(self,r,i):
#         self.real=r
#         self.imaginary=i
#     def __add__(self, other):
#        return str(self.real + other.real) + "+" + str(self.imaginary + other.imaginary) + "i"
# c1=complexnumber(1,3)
# c2=complexnumber(7,8)
# print(c1+c2)
'''8+11i'''

# class person:
#     def __init__(self,n,a):
#         self.name=n
#         self.age=a
#     def __gt__(self, other):
#         if self.age > other.age:
#             return True
#         else:
#             return False
# c1=person("ram",3)
# c2=person("shyam",8)
# if c1>c2:
#     print(f"{c1.name} will pay the bill")
# else:
#     print(f"{c2.name} will pay the bill")
'''shyam will pay the bill'''

'''********************* method overloading and method overriding***************************'''
'''python does not support the overloading concept'''
'''method overloading is a compile time polymorphism'''
# class demo:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
#
# d=demo()
# print(d.add(2,6))
# print(d.add(3,5,6))

'''TypeError: demo.add() missing 1 required positional argument: 'c'''

# class demo:
#
#     def add(self,a,b,c=0):
#         return a+b+c
#
# d=demo()
# print(d.add(2,6))
# print(d.add(3,5,6))
'''8
14'''

# class demo:
#
#     def add(self,*args):
#         total=0
#         for i in args:
#             total +=i
#         return  total
#
# d=demo()
# print(d.add(2,6))
# print(d.add(3,5,6))
# print(d.add(3,4,5,6,7,8,9,10))
'''8
14
52'''

'''method overriding ia run time polymorphism'''
class father:
    def sleep(self):
        print(f"sleep from 10:00 pm to 05:00 am")
    def eat(self):
        print(f"eating")

class son(father):
    def sleep(self):
        print(f"sleep from 12:00 pm to 08:00 am")
        super().sleep()
    def eat(self):
        print(f"bathing")

ram=son()
ram.sleep()
'''sleep from 12:00 pm to 08:00 am
sleep from 10:00 pm to 05:00 am'''