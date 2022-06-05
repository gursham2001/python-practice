import random

win = "you win!"
lose = "you lose!"

user_wins = 0
computer_wins = 0
possible_inputs = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter a choice (Rock, Paper, Scissors) or Q to quit: ").lower()

    computer_choice = random.choice(possible_inputs)

    if user_input == "q":
        break

    if user_input not in possible_inputs:
        continue

    print(f"Computer chose {computer_choice}")

    if user_input == computer_choice:
        print("It's a draw")
    elif user_input == "rock" and computer_choice == "scissors":
        print(win)
        user_wins += 1
    elif user_input == "scissors" and computer_choice == "paper":
        print(win)
        user_wins += 1
    elif user_input == "paper" and computer_choice == "rock":
        print(win)
        user_wins += 1
    else:
        print(lose)
        computer_wins += 1

print(f"\n\nThanks for playing \n\nThe user won {user_wins} times\nThe computer won {computer_wins} times\n\nBye")