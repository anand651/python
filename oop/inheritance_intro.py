# class human:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work")
#
# class male:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work")
# male_1=male()
# male_1.eat()
'''i can eat'''

# class human:
#     def __init__(self,num_heart):
#         self.num_eyes=2
#         self.num_nose=1
#         self.num_heart=num_heart
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work")
#
# class male(human):
#     def __init__(self,name,heart):
#         super().__init__(heart)    # to access the attribute of class human
#         self.name=name
#
#     def flirt(self):
#         print("i can flirt")
#     def work(self):
#         super().work()
#         print("i can code")      # this is overriding concept
#     def display(self):
#         print(f"hi i am {self.name} and i have {self.num_heart} heart")
#
# male_1=male("akash",1)
# male_1.eat()
# male_1.work()
# male_1.flirt()
# print(male_1.num_nose)
# print(male_1.num_eyes)
# print(male_1.name,male_1.num_heart)
# male_1.display()
'''i can eat
i can work
i can code
i can flirt
1
2
akash 1
hi i am akash and i have 1 heart'''

'''######################## types of inheritance ################################'''
'''single inheritance - one parents one child
multiple inheritance - more than one parents one child
multilevel inheritance - grand_father --> father --> son
hierarchical inheritance - one parents more than one child
hybrid inheritance - hierarchical inheritance +  multiple inheritance
'''

'''######################## multiple inheritance ########################'''
# class human:
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work")
# class male:
#     def flirt(self):
#         print("i can flirt")
#     def work(self):
#         print("i can code")
# class boy(human,male):
#     def sleep(self):
#         print("i can sleep")
#     def work(self):
#         print("i can test")
#
# boy_1=boy()
# boy_1.flirt()       #i can flirt
# boy_1.work()        #i can work                                         those who come first
# male.work(boy)       #i can code
#                      #first of all work can search in the boy class , those who can come first is search
# boy_1.work()         #i can test
# print(boy.mro())
'''[<class '__main__.boy'>, <class '__main__.human'>, <class '__main__.male'>, <class 'object'>]'''


# class human:
#     def __init__(self,num_heart):
#         print("calling init from human")
#         self.num_eyes=2
#         self.num_nose=1
#         self.num_heart=num_heart
#     def eat(self):
#         print("i can eat")
# class male:
#     def __init__(self,name):
#         print("calling from male")
#         self.name=name
#     def flirt(self):
#         print("i can flirt")
#     def work(self):
#         print("i can code")
# class boy(human,male):
#     def __init__(self,name,heart,language):
#         human.__init__(self,heart)
#         male.__init__(self,name)
#         self.language=language
#     def sleep(self):
#         print("i can sleep")
#     def display(self):
#         print(f"hye i am {self.name} and i work on the {self.language}")

#boy_1=boy()
# boy_1.work()    #i can code
#print(boy_1.num_nose)
#print(boy_1.name)   # error because first name attribute can search in boy then then search who can come first
              # in human class then found init function (AttributeError: 'boy' object has no attribute 'name')

# boy_1=boy("rahul")
# print(boy_1.num_nose)
'''calling init from human
calling from male
1'''

# boy_1=boy("rahul",1,"python")
# print(boy_1.num_nose)
# print(boy_1.num_heart)
# print(boy_1.language)
# boy_1.display()
'''calling init from human
calling from male
1
1
python
hye i am rahul and i work on the python'''



''' ################### multilevel inheritance  #########################'''

''' parent  --- grand parent
    child 1 --- parent
    child 2 --- son/daughter'''

# class human(object):
#     can_breadth=True
#     def __init__(self,num_heart):
#         print("calling from human class")
#         self.eyes=2
#         self.heart=num_heart
#     def eat(self):
#         print("i can eat")
#     def work(self):
#         print("i can work")
# class male(human):
#     def __init__(self,name):
#         print("calling from male class")
#         self.name=name
#     def sleep(self):
#         print("i can sleep")
# class boy(male):
#     def __init__(self,heart,name,can_dance):
#         human.__init__(self,heart)
#         male.__init__(self,name)
#         self.know_dancing=can_dance
#     def work(self):
#         human.work(self)
#         # super().work()
#         print("i can code")


# boy_1=boy(1)
# boy_1.eat()
# boy_1.work()
# print(boy_1.eyes)
# print(boy.mro())
'''calling from human class
i can eat
i can work
i can code
2
[<class '__main__.boy'>, <class '__main__.male'>, <class '__main__.human'>, <class 'object'>]'''

# boy_1=boy(1,"rahul",True)
# print(boy_1.know_dancing)
# print(boy_1.name)
# print(boy_1.can_breadth)
# print(boy.mro())
'''calling from human class
calling from male class
True
rahul
True
[<class '__main__.boy'>, <class '__main__.male'>, <class '__main__.human'>, <class 'object'>]'''

''' ##################### hierarchical inheritance ######################'''
''' ##################### parent ######################
                        /    /    /
                       /    /    /
                child1  child2  child3'''

# class human(object):
#     def __init__(self,name,age):
#         print("calling from human")
#         self.name=name
#         self.age=age
#     def showdetails(self):
#             print(f"name: {self.name}, age: {self.age}")
#     def eat(self):
#         print("i can eat")
# class male(human):
#     def __init__(self,m_name,age,location):
#         print("calling from male class")
#         human.__init__(self,m_name,age)
#         self.loction=location
#     def sleep(self):
#         print("i can sleep")
# class female(human):
#     def __init__(self,name,age,can_dance):
#         print("calling from female")
#         super().__init__(name,age)
#         self.know_dance=can_dance
#     def showdetails_f(self):
#         human.showdetails(self)
#         print(f"know_dancing: {self.know_dance}")
#     def work(self):
#         print("i can code")
#
# female_1=female("jiya",21,True)
# female_1.eat()
# print(female_1.age)
# female_1.showdetails_f()
#
# male_1=male("anand",18,"patna")
# male_1.sleep()
# male_1.eat()
#
# print(male_1.name)
# print(male.mro())
'''calling from female
calling from human
i can eat
21
name: jiya, age: 21
know_dancing: True

calling from male class
calling from human
i can sleep
i can eat
anand
[<class '__main__.male'>, <class '__main__.human'>, <class 'object'>]'''

''' ######################## hybrid inheritance #############################'''

# class a:
#     def display(self):
#         print("display from a class")
# class b(a):
#     def display(self):
#         print("display from b class")
# class c:
#     def show(self):
#         print("hi from c class")
# class d(b,c):
#     def display(self):
#         print("display from d class")
#
# d1=d()
# d1.display()
# print(d.mro())
'''display from d class
[<class '__main__.d'>, <class '__main__.b'>, <class '__main__.a'>, <class '__main__.c'>, <class 'object'>]'''

'''################# dimond problem #################'''
# class a:
#     def display(self):
#         print("display from a class")
# class b(a):
#     def display(self):
#         print("display from b class")
# class c(a):
#     def show(self):
#         print("hi from c class")
#     def display(self):
#         print("display from c class")
# class d(b,c):
#     pass
#     # def display(self):
#     #     print("display from d class")
#
# d1=d()
# d1.display()
# print(d.mro())
'''display from b class
[<class '__main__.d'>, <class '__main__.b'>, <class '__main__.c'>, <class '__main__.a'>, <class 'object'>]'''

# class a:
#     def display(self):
#         print("display from a class")
# class b:
#     def display(self):
#         print("display from b class")
# class c:
#     def display(self):
#         print("display from c class")
# class d:
#     def display(self):
#         print("display from d class")
# class e:
#     def display(self):
#         print("display from e class")
# class f(a,b,c):
#     def display(self):
#         print("display from f class")
# class g(d,b,e):
#     def display(self):
#         print("display from g class")
# class h(d,a):
#     def display(self):
#         print("display from h class")
# class z(f,g,h):
#     def display(self):
#         print("display from z class")
# z1=z()
# z1.display()
# print(z.mro())
# print(z.__mro__)

'''display from z class
[<class '__main__.z'>, <class '__main__.f'>, <class '__main__.g'>, <class '__main__.h'>, <class '__main__.d'>, <class '__main__.a'>, <class '__main__.b'>, <class '__main__.c'>, <class '__main__.e'>, <class 'object'>]
(<class '__main__.z'>, <class '__main__.f'>, <class '__main__.g'>, <class '__main__.h'>, <class '__main__.d'>, <class '__main__.a'>, <class '__main__.b'>, <class '__main__.c'>, <class '__main__.e'>, <class 'object'>)
'''