# print("hiii")
# print(dir())
# print(__name__)
'''hiii
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
__main__'''

def display(name):
    return name
def do_something():
    print("this function is doing something")
if __name__=="__main__":
   print("this is name.py")
   name = input("enter your name")
   print(display(name))
   do_something()

