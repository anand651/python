import random
letter = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',
          'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
number = ['0','1','2','3','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')','_','+']
print("welcome to password generator!")
n_letter = int(input("how many letter you want in your password"))
n_number = int(input("how many number you want in your password"))
n_symbol = int(input("how many symbol you want in your password"))
password_list= []
for i in range(0,n_letter):
    alphabet = random.choice(letter)
    password_list+=alphabet
for i in range(1,n_number+1):
    code = random.choice(number)
    password_list+=code
for i in range(1,n_symbol+1):
    special = random.choice(symbol)
    password_list+=special
print(password_list)
random.shuffle(password_list)
print(password_list)
password =""
for cha in password_list:
    password+=cha
print(password)
'''welcome to password generator!
how many letter you want in your password4
how many number you want in your password3
how many symbol you want in your password2
['Q', 'D', 'S', 'f', '7', '2', '8', '@', '#']
['@', 'D', '8', '2', 'Q', '7', '#', 'S', 'f']
@D82Q7#Sf'''
