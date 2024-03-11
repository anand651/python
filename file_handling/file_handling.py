# f1=open("file_1","x")          # for creating a file

# f1=open("file_1")             # dy default read mode
# # f1=open("file_1","r")
# data=f1.read()
# print(data)

# f1=open("file_2","x")

# f1=open("file_3","r")
# data=f1.read()
# print(data)               # error because file is not create

# f1=open("file_2","w")
# f1.write("welcome to jenny lecture")                             # previous content of this file will be erase and
                                                                        # welcome to jenny lecture will be printed

# f1=open("file_3","x")

# f1=open("file_3","r+")
# print(f1.read())
# f1.write(" this is the python course")

# f1=open("file_4","x")

# f1=open("file_4","r+")
# f1.write("hye")
# print(f1.read())

# f1=open("file_5","x")

# f1=open("file_5","r+")
# print(f1.tell())    # position of the cursor
# f1.write("hye")
# print(f1.tell())
# print(f1.read())
# print(f1.tell())


# f1=open("file_6","w+")   # automatically file will be created
# f1.close()

# f1=open("file_7","x")

# f1=open("file_7","w+")            # previous content of this file will be erase
# print(f1.tell())
# f1.write("hye i am anand")
# print(f1.tell())
# f1.write("this is the python course")
# print(f1.tell())
# f1.seek(0)                    # cursor will become 0(zero) position
# print(f1.tell())
# data=f1.read()
# print(data)
# print(f1.tell())
# f1.close()

# in append mode we can write only end of the file
# f1=open("file_8","a")             # by default file will be created
# f1.write("hello student")
# #f1.read()                         # error

# f1=open("file_9","a+")
# print(f1.tell())
# f1.write("hello student")
# f1.seek(0)
# print(f1.read())

# f1=open("IMG_20211104_204613.jpg","rb")
# print(f1.read())

f1=open("image_1.jpg","rb")                   # rb mean read binary
f2=open("image_2.jpg","wb")
for i in f1:
    f2.write(i)