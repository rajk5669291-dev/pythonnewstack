def game():
    user = input("Enter rock, paper, scissors or exit: ")
    computer = input("Enter computer choice (rock/paper/scissors): ")

    

    if user == computer:
        print("Tie")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win")

    else:
        print("Computer Wins")

    game()   # recursive call

game()
