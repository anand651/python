# def display():
#     pass
# print(type(display))
'''<class 'function'>'''

# print('HELLo'.lower())         #hello

# class InstructorInfo:
#     pass
#
# instructor_1=InstructorInfo()
# print(type(instructor_1))
'''<class '__main__.InstructorInfo'>'''


# class instructor:
#     def __init__(self):
#         print("creating a new object")
#
# instructor_1=instructor()
# instructor_1.name="payal"
# instructor_1.address="delhi"
# print(instructor_1.name)
# print(instructor_1.address)
# instructor_2=instructor()
# instructor_2.name="jenny"
# instructor_2.address="delhi"
# print(instructor_2.name)
# print(instructor_2.address)
'''creating a new object
payal
delhi
creating a new object
jenny
delhi'''

# class instructor:
#     def __init__(self,instructor_names,addresss):
#         self.name=instructor_names
#         self.address=addresss
#         self.follower=0
#
# instructor_1=instructor("jenny","gurgaon")
# instructor_2=instructor("jenny","delhi")
# print(instructor_1.name,instructor_1.address,instructor_1.follower)
# print(instructor_2.name,instructor_2.address)
'''jenny gurgaon 0
jenny delhi'''

# class instructor:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#         self.followers=0
#     def display(self,subject_teach):
#         print(f"hi ,i am {self.name} and i teach {subject_teach}")
#     def update_follower(self,follower_name):
#         self.followers +=1
#
# instructor_1=instructor("jenny","gurgaon")
# print(instructor_1.name)
# instructor_1.display("python")
# instructor_1.update_follower(("payal"))
# print(instructor_1.followers)
#
# instructor_2=instructor("jiya","gurgoan")
# instructor_2.update_follower("jenny")
# print(instructor_2.followers)
'''jenny
hi ,i am jenny and i teach python
1
1'''

# class circle:
#     def __init__(self,radius):
#         self.pi=3.14
#         self.radius=radius
#     def area(self):
#         return self.pi*self.radius*self.radius
#     def get_circumferance(self):
#         return 2*self.pi*self.radius
#
# circle_1=circle(7)
# a=circle_1.area()
# print(a)
# cir=circle_1.get_circumferance()
# print(cir)
# circle_2=circle(2)
# b=circle_2.area()
# bir=circle_2.get_circumferance()
# print(b,bir)

'''153.86
43.96
12.56 12.56'''

