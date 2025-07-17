import random

symbols = ["🍒", "🍋", "🔔", "💎", "⭐️"]

def spin_row():
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        print("JACKPOT!")
        return bet * 5
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print("You got a match!")
        return bet * 2
    else:
        print("No match.")
        return 0

def main():
    balance = 100
    print("Welcome to the Slot Machine ")
    print(f"Your starting balance is £{balance}\n")

    while balance > 0:
        try:
            bet = int(input("Enter your bet (0 to quit): £"))
            if bet == 0:
                print("Thanks for playing!")
                break
            if bet > balance:
                print("You can't bet more than your balance!")
                continue

            balance -= bet
            row = spin_row()
            print_row(row)
            winnings = get_payout(row, bet)
            balance += winnings
            print(f"New balance: £{balance}\n")

        except ValueError:
            print("Please enter a valid number.\n")

    if balance <= 0:
        print("You're out of money. Game over!")

if __name__ == '__main__':
    main()
