# Rock Paper Scissors Game
# Created during CodSoft Virtual Internship

import random

print("=== ROCK PAPER SCISSORS ===")
print("Choices: rock, paper, scissors")

user_choice = input("Enter your choice: ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a Tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You Win!")
else:
    print("You Lose!")