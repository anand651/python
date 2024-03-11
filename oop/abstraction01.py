from abstraction02 import vehicle
class bike(vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color=color
    def start(self):
        print("start with kick")
    def display(self):
        print(f"my color is {self.color}")
class scooty(vehicle):
    def __init__(self,n):
        super().__init__(n)
    def start(self):
        print("self start")
class car(vehicle):
    def __init__(self,n,x):
         super().__init__(n)
         self.no_of_gears=6
    def start(self):
        print("start with key")