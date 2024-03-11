import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1=float(input("enter first number : "))
    for symbol in operations_dict:
        print(symbol)

    continue_flag=True
    while continue_flag:
        op_symbol=input("pick an operation : ")
        number2=float(input("enter the next number"))
        calculator_function=operations_dict[op_symbol]
        output=calculator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue=input(f"enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit").lower()
        if should_continue=='y':
            number1=output
        elif should_continue=='n':
            continue_flag=False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("bye")

calculator()


'''enter first number : 3
+
-
*
/
pick an operation : +
enter the next number5
3.0 + 5.0 = 8.0
enter 'y' to continue calculation with 8.0 or 'n' to start a new calculation or 'x' to exity
pick an operation : *
enter the next number2
8.0 * 2.0 = 16.0
enter 'y' to continue calculation with 16.0 or 'n' to start a new calculation or 'x' to exit'''

'''enter first number : 9
+
-
*
/
pick an operation : /
enter the next number3
9.0 / 3.0 = 3.0
enter 'y' to continue calculation with 3.0 or 'n' to start a new calculation or 'x' to exitx
bye

Process finished with exit code 0
'''