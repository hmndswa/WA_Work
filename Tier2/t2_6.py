import math

while True:
    print("\n-----Menu-----")
    print("1.--Addition--")
    print("2.-Square Root-")
    print("3.---Quit---")

    try:
        menu = int(input("Enter choice: "))
        
        if menu == 1:
            num1 = int(input("Enter first number to be added: "))
            num2 = int(input("Enter second number to be added: "))
            addition = num1 + num2
            print(f"Result of addition = {addition}")

        elif menu == 2:
            number = float(input("Enter a number to find the square root: "))
            if number < 0:
                print("Cannot find square root of a negative number!")
            else:
                square_root = math.sqrt(number)
                print(f"Result of Square root = {square_root}")

        elif menu == 3:
            print("Exiting program. Goodbye!")
            break

        else:
            print("Unknown choice, try again!")

    except ValueError:
        print("Invalid input! Please enter numbers only.")


    #stuck at looping back to the menu - done
    #tryandcatch exceptions - done