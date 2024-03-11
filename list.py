number = [1,3,2,4,-7,0,6]
numbers = ['jenny','khatri','hello','anand','kumar']
mix_list = [1,'jenny',True,10.323]
# print(number)                                #[1, 3, 2, 4, -7, 0, 6]
# print(numbers)                               #['jenny', 'khatri', 'hello', 'anand', 'kumar']
# print(mix_list)                              #[1, 'jenny', True, 10.323]

# print(number[5])                             #0   5 is the index number of number
# print(number[-2])                            #0   last second is the index number of number
# print(number[0:4])                           #[1, 3, 2, 4]
# print(number[0:])                            #[1, 3, 2, 4, -7, 0, 6]
# print(number[:])                             #[1, 3, 2, 4, -7, 0, 6]
# print(number[1:4])                           #[3, 2, 4]
# print(number[1:0])                           #[]
# print(number[0:4:2])                         #[1, 2]
# print(number[0:5:2])                         #[1, 2, -7]
# print(number[0::3])                          #[1, 4, 6]
#
# print(number.sort())                           #error none   because it doesnot return the value
#
# number.sort()
# print(number)                                   #[-7, 0, 1, 2, 3, 4, 6]

number.reverse()
# print(number)                                     #[6, 4, 3, 2, 1, 0, -7]
# print(max(number))                                #6
# print(min(number))                                #-7

# mix_list.sort()                        #error    '<' not supported between instances of 'str' and 'int'
# print(mix_list)

number.append(687)
# print(number)                                   #[6, 4, 3, 2, 1, 0, -7, 687]

number.insert(2,56)
# print(number)                                   #[6, 4, 56, 3, 2, 1, 0, -7, 687]

number.extend([-0, -9, -7])
# print(number)                                   #[6, 4, 56, 3, 2, 1, 0, -7, 687, 0, -9, -7]

number[1]=9
# print(number)                                   #[6, 9, 56, 3, 2, 1, 0, -7, 687, 0, -9, -7]

number[1:4]=[8,55,2]
# print(number)                                   #[6, 8, 55, 2, 2, 1, 0, -7, 687, 0, -9, -7]

number.remove(2)
# print(number)                                   #[6, 8, 55, 2, 1, 0, -7, 687, 0, -9, -7]

abc=number.pop()
# print(number)                                  #[6, 8, 55, 2, 1, 0, -7, 687, 0, -9]
# print(abc)                                     #-7

number.pop(3)
# print(number)                                   #[6, 8, 55, 1, 0, -7, 687, 0, -9]