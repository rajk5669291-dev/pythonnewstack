import random

def game():
    user = input("Enter (rock/paper/scissors): ")

    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    print("Computer:", computer)

    if user == computer:
        print("Tie")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win")
    else:
        print("Computer Wins")

    game()

game()
