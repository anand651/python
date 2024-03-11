# list1=[1,2,3,7]
# print(len(list1))
# print(list1)
# print(type(list1))
'''4
[1, 2, 3, 7]
<class 'list'>'''

# class demo:
#     name="jenny"
# d=demo()
# print(len(d))
# print(d)
'''error'''

# class author:
#     def __init__(self,name,book_name,pages):
#         self.name=name
#         self.book_name=book_name
#         self.pages=pages
#
# d=author("jenny","python basic to advance",300)
# print(d)
'''<__main__.author object at 0x0000022153519220>'''

class author:
    def __init__(self,name,book_name,pages):
        self.name=name
        self.book_name=book_name
        self.pages=pages
    def __len__(self):
        return self.pages
    def __str__(self):
        return f"{self.book_name} by {self.name}"
    def __call__(self, *args, **kwargs):
        print("hi")
    def __del__(self):
        print("author object has been deleted")
d=author("jenny","python basic to advance",300)
print(len(d))
print(d)
print(dir(int))
d()
del d
print(d)
'''300
python basic to advance by jenny
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
hi
author object has been deleted
Traceback (most recent call last):
  File "C:\Users\DELL\PycharmProjects\pythonProject2\magic_dunder_method.py", line 45, in <module>
    print(d)
          ^
NameError: name 'd' is not defined. Did you mean: 'id'?'''
