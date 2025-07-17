def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")
    
def deposit():
    amount = float(input("Enter the amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:    
        print("That's not a valid amount.")
    else:
        return amount
    
def main():
    balance = 0
    is_running = True
    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance+= deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            print("Exiting the program.")
            is_running = False
        else:
            print("Invalid choice. Please try again.")
            print("Thank You! Have a nice day")

if __name__ == "__main__":
    main()