import random
choice_for_game = ["Paper", "Scissors", "Rock"]
random_choice = random.choice(choice_for_game)
user_choice = input("Please enter paper,scissors or rock: ")
if random_choice == "Paper":
    if user_choice == "paper":
        print("Draw")
    elif user_choice == "scissors":
        print("You win")
    elif user_choice =="rock":
        print("Computer Wins")
    else:
        print("Please enter heads,tails and rocks correctly.")
elif random_choice == "Scissors":
    if user_choice == "scissors":
        print("Draw")
    elif user_choice == "rock":
        print("You win")
    elif user_choice =="paper":
        print("Computer Wins")
    else:
        print("Please enter heads,tails and rocks correctly.")
elif random_choice == "Rock":
    if user_choice == "rock":
        print("Draw")
    elif user_choice == "paper":
        print("You win")
    elif user_choice =="scissors":
        print("Computer Wins")
    else:
        print("Please enter heads,tails and rocks correctly.")
print(f"Computer had choosen {random_choice}")
