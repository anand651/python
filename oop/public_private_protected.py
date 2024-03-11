# class student:
#     def __init__(self,name):
#         self.name=name
#     def display(self):
#         print(f"hi myself {self.name} from student class")
# s1=student("rahul")
# print(s1.name)
# s1.display()
'''rahul
hi myself rahul from student class'''

# class student:
#     def __init__(self,name,rollno):
#         self.name=name                                    #public instance variable
#         self._rollno=rollno                               #protected instance variable
#     def display(self):
#         print(f"hi myself {self.name} wit rollno {self._rollno} from student class")
#
# class branch(student):
#     pass
# # b1=branch()          # error because in branch class init function is not found
#
# def showdata():
#  b1=branch("nisha",45)
#  print(b1.name)
#  print(b1._rollno)
#  b1.display()
#
# showdata()
'''nisha
45
hi myself nisha wit rollno 45 from student class'''

class student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age
    def __display(self):
        print(f"hi myself {self.name} wit rollno {self._rollno} and {self.__age} from student class")
    def displayprivatedata(self):
        self.__display()

class branch(student):
    def show(self):
        print(f"my age is {self._rollno}")

b1=branch("nisha",45,89)
# print(b1.__age)
# b1.show()

# def showdata():
#  b1=branch("nisha",45)
#  print(b1.name)
#
# showdata()

s1=student("rahul",23,18)
# s1.name="raunak"
# s1._rollno=90
# print(s1.__age)          # error
# s1.display()

'''################## name mangling method ############################'''
# print(dir(s1))
# s1.displayprivatedata()
'''['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__weakref__', '_rollno', '_student__age', '_student__display', 'displayprivatedata', 'name']
hi myself rahul wit rollno 23 and 18 from student class'''

print(s1._student__age)
s1._student__display()
'''18
hi myself rahul wit rollno 23 and 18 from student class'''

s1._student__age=45
print(s1._student__age)
s1._student__display()
'''45
hi myself rahul wit rollno 23 and 45 from student class'''



'''********************* there are three method to acess the private member of the class
1. we can define private attribute in the public section
2. name mangling method
3. getter and setter method'''