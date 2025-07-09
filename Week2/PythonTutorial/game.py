import random

def get_choices():
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    while player_choice not in choices:
        print("Invalid input. Try again.")
        player_choice = input("Enter rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)
    return player_choice, computer_choice

def decide_winner(player, computer):
    print(f"\nYou chose: {player} and Computer chose: {computer}")
    
    if player == computer:
        return "It's a tie!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "scissors" and computer == "paper") or
        (player == "paper" and computer == "rock")
    ):
        return "You win!"
    else:
        return "Computer wins!"

player_choice, computer_choice = get_choices()
result = decide_winner(player_choice, computer_choice)
print(result)