def add(num1,num2):
    print(num1 + num2)
def multiply(num1,num2):
    print(num1 * num2)
def divide(num1,num2):
    print (num1 / num2)
def subtract(num1,num2):
    print (num1 - num2)
   
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))
choice = input("Enter x for multiply, + for addition / for division and - for subtraction ")
if choice == "x":
    multiply(number1,number2)
elif choice == "/":
    divide(number1,number2)
elif choice == "-":
    subtract(number1,number2)
elif choice == "+":
    add(number1,number2)
else:
    print ("Not a valid choice, try again!")
