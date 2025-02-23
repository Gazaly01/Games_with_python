# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------
# ?                                                                     --------2---------
#!----------------------------------------------------------------------  Number Guessing ------------------------------------------------------------------------
# ?                                                                     --------2---------
# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------


import random

top_of_range = input("Type A Number Please: ")
# another way & easy -> put int(input)

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Pleaes input a number larger than 0 next time.")
        quit()
else:
    print("Please Type a number next time.")
    quit()

random_number = random.randrange(top_of_range)
# randint include the 2 values randint(1,5) and not optional to put start point like randrange, but randrange don't include the stop point like indexing and slicing
# print(random_number)

guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    # else: # i could use elif (better than else)
    # print("You got it wrong -_-")
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were bolow the number!")

print(f"You got it in {guesses} guesses")
