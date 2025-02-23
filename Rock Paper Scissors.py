# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------
# ?                                                                     --------3---------
#!---------------------------------------------------------------------- Rock Paper Scissors ------------------------------------------------------------------------
# ?                                                                     --------3---------
# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input in ["q", "quit"]:
        # quit() # or break
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    print(f"Computer Picked: {computer_pick}")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        continue
    elif user_input == computer_pick:
        print("Draw Up")
        user_wins += 1
        computer_wins += 1

    # Computer Win

    else:
        print("You lost")
        computer_wins += 1

print("GoodBye!")
print(f"You Won {user_wins} times")
print(f"Computer Won {computer_wins} times")
