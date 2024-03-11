''''dictionary is case sensetive'''

# phone_no={
#     'ram':1234,
#     'shyam':5678,
#     'radha':9012,                  # in this line comma is not complasary
# }
# print(phone_no)                       #{'ram': 1234, 'shyam': 5678, 'radha': 9012}
# print(phone_no['shyam'])              #5678

# phone_no={
#     'ram':1234,
#     'shyam':5678,
#     'radha':9012,
#     'ram':66666
# }
# print(phone_no)             #{'ram': 66666, 'shyam': 5678, 'radha': 9012}


phone_no=dict({
    'ram': 6666,
    'shyam': 5678,
    'radha': 9012,
})
# print(phone_no)               #{'ram': 6666, 'shyam': 5678, 'radha': 9012}
#
# phone_no['shyam']=1111
# print(phone_no)                #{'ram': 6666, 'shyam': 1111, 'radha': 9012}
#
# phone_no['mohan']={1112,1256,987}
# phone_no['shyam']={'shyam_home':9876,'shyam_work':4444}
# print(phone_no)                #{'ram': 6666, 'shyam': {'shyam_home': 9876, 'shyam_work': 4444},
#                                           # 'radha': 9012, 'mohan': {1112, 1256, 987}}
#
# print(phone_no['shyam'])                  #{'shyam_home': 9876, 'shyam_work': 4444}
# print(phone_no['shyam']['shyam_home'])    #9876
# print(phone_no.get('ram'))                #6666
#
# del phone_no['ram']                   #  it cannot return the value
# print(phone_no)                       #{'shyam': {'shyam_home': 9876, 'shyam_work': 4444}, 'radha': 9012,
#                                                  # 'mohan': {1112, 1256, 987}}
#
# phone_no.pop('radha')                 #  it can return the value
# print(phone_no)                        #{'shyam': {'shyam_home': 9876, 'shyam_work': 4444},
#                                                # 'mohan': {1112, 1256, 987}}
#
# print(phone_no.keys())                     #dict_keys(['shyam', 'mohan'])
# print(phone_no.values())                  #dict_values([{'shyam_home': 9876, 'shyam_work': 4444}, {1112, 1256, 987}])
#
# print(phone_no.items())#dict_items([('shyam', {'shyam_home': 9876, 'shyam_work': 4444}), ('mohan', {1112, 1256, 987})])
# print(phone_no.popitem())             #('mohan', {1112, 1256, 987})
# print(phone_no)                       #{'shyam': {'shyam_home': 9876, 'shyam_work': 4444}}
#
#
#  #print(phone_no.clear())             #None
# print(phone_no)                         #{'shyam': {'shyam_home': 9876, 'shyam_work': 4444}}
# print(len(phone_no))                     #1

# for i in phone_no:
#     print(i)
#     print(phone_no[i])
'''ram
6666
shyam
5678
radha
9012'''

# for i in phone_no.items():
#     print(i)
'''('ram', 6666)
('shyam', 5678)
('radha', 9012)'''

# data={
#     1:'jenny',
#     2:'ram',
#     0:'mohan'
# }
# print(data[0])                 #mohan
#
# phone_no=data.copy()
# print(phone_no)                #{1: 'jenny', 2: 'ram', 0: 'mohan'}

student_data=[
    {
        "name":"ram",
        "roll_no":10,
        "age":20,
        "course":"python"
    },
    {
        "name":"mohan",
        "roll_no":11,
        "age":22,
        "course":"java",
    }
]

def add_new_student(name,rollno,age,course_option):
    new_student={}
    new_student["name"]=name
    new_student["roll_no"]=rollno
    new_student["age"]=age
    new_student["course"]=course_option
    student_data.append(new_student)

add_new_student("shyam",22,18,"c++")
print(student_data)                     #[{'name': 'ram', 'roll_no': 10, 'age': 20, 'course': 'python'},
                                            # {'name': 'mohan', 'roll_no': 11, 'age': 22, 'course': 'java'},
                                                # {'name': 'shyam', 'roll_no': 22, 'age': 18, 'course': 'c++'}]