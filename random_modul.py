import random
a=random.randint(1,7)
# print(a)
'''randint means both 1 and 7 between included'''

b=random.randrange(1,7)
# print(b)
'''randrange means 1 to 6 included but 7 not included'''

c=random.random()
# print(c)
'''random means 0.0<=x<1.0 '''

d=random.uniform(1,3)
# print(d)
'''uniform mean 1.0<=x<3.0'''

l=[2,5,90,-5,89,12,56]
e=random.choice(l)
# print(e)
'''choice means random number choose from the list'''

random.shuffle(l)
# print(l)
'''shuffle means changing the index number of all the number from the list'''

# side = random.randint(0,1)
# if side==0:
#     print("head",side)
# else :
#     print("tail",side)
'''tail 1'''

# text = "welcome to jenny's lectures"
# splited_text=text.split("e")
# print(splited_text)
'''['w', 'lcom', ' to j', "nny's l", 'ctur', 's']'''

'''************ without random choice used,we can find the who will pay the bill **************'''

# names=input("enter everybody's name seperated by comma:")
# names_list=names.split(",")
# print(names_list)
# length= len(names_list)
# print(length)
# random_choice=random.randint(0,length-1)
# print(f"{names_list[random_choice]} will pay the bill")
'''enter everybody's name seperated by comma:anand,raja,dezy,khushi
['anand', 'raja', 'dezy', 'khushi']
4
dezy will pay the bill'''

# names=input("enter everybody's name seperated by comma:")
# names_list=names.split(",")
# person_selected=random.choice(names_list)
# print(f"{person_selected} will pay the bill")
'''enter everybody's name seperated by comma:anand,dezy,khushi,raja
anand will pay the bill'''