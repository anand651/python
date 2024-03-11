class student:
    def __init__(self,name,rollno,age):
        self.name=name
        self._rollno=rollno
        self.__age=age

    '''################## getters and setters method ################'''

    def get_age(self):        #   get_age is a function name
        return self.__age
    def set_age(self,age):        #   set_age is a function name
        if age>35:
            print(f"invalid age given ... age should be less than 35 ")
        else:
            self.__age=age

#     def __display(self):
#         print(f"hi myself {self.name} {self.__age} years old with rollno {self._rollno} from student class")
#     def displayprivatedata(self):
#         self.__display()
#
# class branch(student):
#     def show(self):
#         print(f"my rollno is {self._rollno}")


s1=student("rahul",23,20)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())
'''20
34'''