class bank_account:
    def __init__(self,name,balance):
        self.account_holder=name
        self.balalnce=balance
    def deposite(self,amount):
        self.balalnce=self.balalnce + amount
        print(f"deposited {amount} to your account")
    def __str__(self):
        return f"account holder name : {self.account_holder} \nbalance : {self.balalnce}"
    def withdraw(self,amount):
        if amount > self.balalnce:
            print("not enough money")
        else:
            self.balalnce=self.balalnce - amount
            print(f"{amount} money can be withdraw from your account")
obj=bank_account("ramesh",1000)
print(obj)
obj.deposite(200)
print(obj)
obj.withdraw(300)
print(obj)