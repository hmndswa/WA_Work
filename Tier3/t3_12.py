import math

def addition():
    num1 = int(input("Enter first number to be added: "))
    num2 = int(input("Enter second number to be added: "))
    result = num1 + num2
    print(f"Result of addition = {result}")

def substraction():
    num1 = int(input("Enter first number to be added: "))
    num2 = int(input("Enter second number to be added: "))
    result = num1 - num2
    print(f"Result of Substraction = {result}")    

def multiply():
    num1 = int(input("Enter first number to be added: "))
    num2 = int(input("Enter second number to be added: "))
    result = num1 * num2
    print(f"Result of multiply = {result}")

def divide():
    num1 = float(input("Enter first number to be added: "))
    num2 = float(input("Enter second number to be added: "))
    result = num1 / num2
    print(f"Result of divide = {result}")
    

while True:
    print("-----Menu-----")
    print("1.--Addition--")
    print("2.-Substraction-")
    print("3.--Multiply--")
    print("4.--Divide--")
    print("5.---Quit---")



    try:
        menu = int(input("Enter choice: "))

        if menu == 1:
            addition()

        if menu == 2:
            substraction()

        if menu == 3:
            multiply()
        if menu == 4:
            divide()
        if menu == 5:
            print("Exiting program. Goodbye!")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")