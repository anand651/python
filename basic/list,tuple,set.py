'''************************************ list=[],tuple=(),set={} *******************'''

'''index start from 0(zero)'''
'''when the index is in -(minus) then last index start from 1'''

list =[10,34,90,[45,78,-3],89,34]
# print(len(list))
# print(list[3][2])
# print(list[-2])
# print(list[len(list)-3])
# print(list[3][::2])
'''6
-3
89
[45, 78, -3]
[45, -3]'''

# list2 = [10,34,90,["ram","mohan","shyam"],89]
# print(list2[3][0])
"""ram"""

# number = [[1,2,3],[4,5,6],[7,8,9]]
# a=input("select a number of 3*3")
# b=input("select a number of 3*3")
# print(number[int(a)-1][int(b)-1])
'''select a number of 3*32
select a number of 3*33
6'''

# row1=['1','2','3']
# row2=['4','5','6']
# row3=['7','8','9']
# matrix=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position= input("enter the position where you want to hide money")
# row_number=int(position[0])
# column_number=int(position[1])
# row_selected=matrix[row_number-1]
# row_selected[column_number-1]='x'
# print(f"{row1}\n{row2}\n{row3}")
'''['1', '2', '3']
['4', '5', '6']
['7', '8', '9']
enter the position where you want to hide money23
['1', '2', '3']
['4', '5', 'x']
['7', '8', '9']'''


# row1=['😀','😀','😵']
# row2=['😀','😀','😵']
# row3=['😀','😀','😵']
# matrix=[row1,row2,row3]
# print(f"{row1}\n{row2}\n{row3}")
# position= input("enter the position where you want to hide money")
# row_number=int(position[0])
# column_number=int(position[1])
# row_selected=matrix[row_number-1]
# row_selected[column_number-1]='x'
# print(f"{row1}\n{row2}\n{row3}")
'''['😀', '😀', '😵']
['😀', '😀', '😵']
['😀', '😀', '😵']
enter the position where you want to hide money33
['😀', '😀', '😵']
['😀', '😀', '😵']
['😀', '😀', 'x']'''

tuple1 = (12,6,-8,'jenny',True,12)
# print(tuple1)                           #(12, 6, -8, 'jenny', True, 12)
# print(tuple1[2])                        #-8
# print(tuple1[-2])                       #True
# print(type(tuple1))                     #<class 'tuple'>
# print(len(tuple1))                      #6

tuple2 =(45)
# print(tuple2)                                #45
# print(type(tuple2))                          #<class 'int'>

tuple2 =(45,)
# print(tuple2)                                #(45,)
# print(type(tuple2))                          #<class 'tuple'>

tuple3 =(45,23,89)
# print(tuple3)                                       #(45, 23, 89)
# print(type(tuple3))                                 #<class 'tuple'>
# tuple4=(tuple1,tuple3)
# print(tuple4)                                       #((12, 6, -8, 'jenny', True, 12), (45, 23, 89))
# print(tuple4[1])                                    #(45, 23, 89)
# print(len(tuple4))                                  #2


tuple4 = tuple1+tuple3
# print(tuple4)                                    #(12, 6, -8, 'jenny', True, 12, 45, 23, 89)
# print(len(tuple4))                               #9
# print(min(tuple3))                               #23
# print(max(tuple3))                               #89
# print(tuple1.count(12))                          #2
# print(tuple1.index(12))                          #0
'''first index will be representation.'''

list1 = [1,2,3,4,5]
# print(tuple(list1))                                #(1, 2, 3, 4, 5)

tuple5 = (10,34)*5
# print(tuple5)                                      #(10, 34, 10, 34, 10, 34, 10, 34, 10, 34)



set2 = {10,34,True,'jenny',10}
# print(set2)                                        #{True, 10, 'jenny', 34}

set1 = {10,34,True,'jenny'}
# print(set1)                                          #{True, 10, 'jenny', 34}
#     # in tuple are inmutable ,it cannot changeable,we cannot change the data,we cannot change the indexing


# set3 = {10,34,68,True,'jenny',1,10}
# print(set3)                         #{True, 34, 68, 10, 'jenny'}         #1 cannot print because true means 1
# print(type(set3))                   #<class 'set'>
# set3.add(99)
# print(set3)                         #{True, 34, 99, 68, 10, 'jenny'}
# print(len(set3))                    #6
# set3.remove(10)
# print(set3)                        #{True, 34, 99, 68, 'jenny'}
# set3.discard(68)
# print(set3)                        #{True, 34, 99, 'jenny'}
# # set3.clear()
# # print(set3)
# set3.pop()
# print(set3)                       #{34, 99, 'jenny'}  # remove random item
# set3.add((16,78,97))
# print(set3)            #{(16, 78, 97), 34, 99, 'jenny'} # tuple can be added in set but list cannot be added in set


# set3.add([16,78,97])
# print(set3)                 # error    list is mutable item. mutable means we can access the value with index number


# set4 = {}
# print(set4)                     #{}
# print(type(set4))               #<class 'dict'>

# set5 = set()
# print(set5)                       #set()
# print(type(set5))                 #<class 'set'>



                              # operation on sets

set1 = {'ram','shyam','jenny'}
set2 = {'jenny','jiya','akash'}
set3 = { 'anand','jenny','khushi'}
# print(set1.union(set2,set3))
# print(set1 | set2 | set3)                           # both operand will be set then the operator work
# print(set1.union(('jenny','mohan'),['raja','mohan']))
# set1.update(set2)
# print(set1)
# set1.update(['Jenny','anand'])
# print(set1)
# set1 |=set2
# print(set1)
'''{'jiya', 'shyam', 'khushi', 'akash', 'ram', 'anand', 'jenny'}
{'jiya', 'shyam', 'khushi', 'akash', 'ram', 'anand', 'jenny'}
{'shyam', 'raja', 'ram', 'jenny', 'mohan'}
{'jiya', 'shyam', 'akash', 'ram', 'jenny'}
{'jiya', 'Jenny', 'shyam', 'akash', 'ram', 'anand', 'jenny'}
{'jiya', 'shyam', 'akash', 'ram', 'jenny', 'Jenny', 'anand'}'''


set1 = {'ram','shyam','jenny'}
set2 = {'jenny','jiya','akash'}
set3 = { 'anand','khushi'}
# print(set1.intersection(set2))
# print(set1.intersection(set2,set3))
# print(set1.intersection(['mohan','shiva']))
# print(set1 & set2)                              # both operand will be set then the operator work
# set1.intersection_update(set2)                    # this will not return anything so we cannot use this line print
# print(set1)
# set1.intersection_update(['mohan','shiva'])        # this will not return anything so we cannot use this line print
# print(set1)
'''{'jenny'}
set()
set()
{'jenny'}
{'jenny'}
set()'''


set1 = {'ram','shyam','jenny'}
set2 = {'jenny','jiya','akash'}
set3 = { 'anand','khushi','shyam'}
# print(set1.difference(set2))                        #{'ram', 'shyam'}
# print(set1.difference(['shyam']))                   #{'ram', 'jenny'}
# print(set1 - set2 - set3 )                          #{'ram'}
# # print(set1 - ['ram'])                             # error
# set1.difference_update(set2)
# print(set1)                                         #{'ram', 'shyam'}


# print(set1.symmetric_difference(set2))                   #{'jiya', 'shyam', 'akash', 'ram'}
# print(set1.symmetric_difference(set2,set3))                  #error

# print(set1 ^ set2 ^ set3)
# set2.symmetric_difference_update(set1)
# print(set2)
'''{'akash', 'jiya', 'khushi', 'ram', 'anand'}
{'akash', 'shyam', 'jiya', 'ram'}'''

# set2.symmetric_difference_update(('mohan','shivam'))
# print(set2)
'''{'akash', 'jiya', 'mohan', 'jenny', 'shivam'}'''


set1 = {'ram','shyam','jenny'}
set2 ={'jiya','akash','jenny'}
# print(set1.isdisjoint(set2))
# print(set1.isdisjoint(['mohan','shiva']))
# print(set1.issubset(['mohan','shiva','ram','shyam','jenny']))
# print(set1.issubset(set2))               # set1 is subset of set2 if everyelements of set1 is in set2
# print(set1 <= set1)
# print(set1.issuperset(set2))           # set1 is superset of set2 if set1 contain every elements of set2
# print(set1 >=set2)
# set2.clear()                  #clear is used to delete the elements of set
# print(set2)
# # del set2                    #del is used to delete the set
# # print(set2)
'''False
True
True
False
True
False
False
set()'''