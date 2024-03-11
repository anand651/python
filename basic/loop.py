''' *********************************** for loop ************************************'''
# name = 'jenny'
# for i in name:
#     print(i)
'''j
e
n
n
y'''

# name = ['jenny','akash','shyam']
# for i in name:
#     print(i)
#     if i=='jenny':
#         print('hey, it is me')
'''jenny
hey, it is me
akash
shyam'''

''' *********************** append mode **************************'''

# list1 = [2,3,5,-2,10]
# squares = []
# for i in list1:
#     square =i**2
#     squares.append(square)
# print("the list of square is :",squares)
'''the list of square is : [4, 9, 25, 4, 100]'''

''' ******************************* for else ********************************'''
'''for else means that forcefully out from the program.'''

# tuple1 = (21,56,90,42,2,-43,-1)
# for i in tuple1 :
#    # print(i)
#     if i%9==0:
#         print(i)
#         break
#     else:
#         print("hello",i)
# else :
#     print("loop have been successfully completed and we are in else block now !!!")
# print("out of for/else")
'''hello 21
hello 56
hello 91
hello 42
hello 2
hello -43
hello -1
loop have been successfully completed and we are in else block now !!!
out of for/else'''

'''********************* split mode ***********************'''

# height = input("enter the all heights separated by a space:")
# height_list = height.split(' ')
# print(height_list)
# count = 0
# for heigh in height_list:
#     count = count+1
# print(count)
# for i in range(count):
#     height_list[i]=int(height_list[i])
# total =0
# for person in height_list:
#     total +=person
# avg = total/count
# print("average height is :",round(avg))
'''enter the all heights separated by a space:3 5 7 8 9
['3', '5', '7', '8', '9']
5
average height is : 6'''

'''********************* without max mode used, we can find the maximun number ******************'''

# number = input("enter list of numbers seperated by space:")
# number_list = number.split()
# print(number_list)
# count=0
# for i in range(0,len(number_list)):
#     number_list[i] =int(number_list[i])
# print(number_list)
# maximun_number = number_list[0]
# for number in number_list:
#     if number>maximun_number:
#         maximun_number=number
# print(f"the maximun number is : {maximun_number}")
'''enter list of numbers seperated by space:4 6 3 8 1 0
['4', '6', '3', '8', '1', '0']
[4, 6, 3, 8, 1, 0]
the maximun number is : 8'''

''' **************************** range function *********************'''

# a = range(2,15,3)
# for i in a:
#     print(i)
'''2
5
8
11
14
'''

# total=0
# for i in range(2,101,2):
#      total+=i
# print(total)
'''2550'''

# total=0
# for i in range(1,101):
#     if i%2==0:
#        total+=i
# print(total)
'''2550'''

# for i in range(1,16):                 # 16 is not included
#     if i%3==0 and i%5==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)
'''1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz'''

'''********************************************** while loop **********************************'''

# count=1
# while count<=5:
#     print(count)
#     count +=1
# print("out from loop")
'''1
2
3
4
5
out from loop'''

# count=5
# while count>0:
#     print(count)
#     count -=1
# print("out from loop")
'''5
4
3
2
1
out from loop'''

'''***************************************** while else ************************************'''

# count=5
# while count>0:
#     print(count)
#     count -=1
# else:
#     print("in else block")
# print("out from loop")
'''5
4
3
2
1
in else block
out from loop'''

# count=5
# while count>0:
#     print(count)
#     count -=1
#     if count ==3:
#         break
# else:                                # else part cannot be executed because we are force fully terminated the loop
#     print("in else block")           #jab condition false karega tab while ka else block work karega
# print("out from loop")
'''5
4
out from loop'''

# count = 1
# while count < 1:
#     print(count)
#     count +=1
# else:
#     print("in else block")
# print("out of the loop")
'''in else block
out of the loop'''

# number = int(input("enter a number (-1 to quit)"))
# while number != -1:
#     print(number)
#     number = int(input("enter a number (-1 to exit)"))
# else:
#     print("in the else block")
# print("out from the loop")
'''enter a number (-1 to quit)5
5
enter a number (-1 to exit)-9
-9
enter a number (-1 to exit)-1
in the else block
out from the loop'''

# count = 0
# while True:
#     print(count)
#     count +=1
#     if count ==5:
#         break
# else:
#     print("in else block")
# print("out of the loop")
'''0
1
2
3
4
out of the loop'''

'''***************sum of all input positive number ****************'''

# number = int(input("enter a number (-1 to quit)"))
# sum=0
# while number != -1:
#     if number > 0:
#         sum +=number
#     number = int(input("enter a number (-1 to exit)"))
# else:
#     print("sum of positive number",sum)
#     print("in the else block")
# print("out from the loop")
'''enter a number (-1 to quit)5
enter a number (-1 to exit)4
enter a number (-1 to exit)3
enter a number (-1 to exit)-9
enter a number (-1 to exit)-8
enter a number (-1 to exit)-1
sum of positive number 12
in the else block
out from the loop'''

'''********************************** break, continue, pass ****************************'''

# count = 1
# while count<=10:
#     print(count)
#     count += 1
#     if count ==7:
#         break
#     print("hi")
# print("out from loop")
'''1
hi
2
hi
3
hi
4
hi
5
hi
6
out from loop'''

# list1 = ["hi","hello","welcome"]
# list2 = ["krishna","ram","madhav"]
# for item in list1:
#     for name in list2:
#         print(item,name)
#         if item=="hello" and name == "ram":
#             break
#     print("out from inner loop")
# print("out of the outer loop")
'''hi krishna
hi ram
hi madhav
out from inner loop
hello krishna
hello ram
out from inner loop
welcome krishna
welcome ram
welcome madhav
out from inner loop
out of the outer loop'''

# list1 = ["hi","hello","welcome"]
# list2 = ["krishna","ram","madhav"]
# for item in list1:
#     for name in list2:
#         if item=="hello" and name == "ram":
#               continue
#         print(item, name)
#     print("out from inner loop")
# print("out of the outer loop")
'''hi krishna
hi ram
hi madhav
out from inner loop
hello krishna
hello madhav
out from inner loop
welcome krishna
welcome ram
welcome madhav
out from inner loop
out of the outer loop'''

# count = 1
# while count <=5:
#     print(count)
#     count+=1
#     if count == 3:
#         pass
#     print("hi")
# print("out of the loop")
'''1
hi
2
hi
3
hi
4
hi
5
hi
out of the loop'''

# for i in range(1,11):
#     pass