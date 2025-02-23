# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------
# ?                                                                     --------4---------
#!---------------------------------------------------------------------- Choose Your Own Adventure ---------------------------------------------------------------
# ?                                                                     --------4---------
# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------

name = input("Type Your Name: ").strip().title()

print(f"Welcome {name} to this adventure")

answer = (
    input(
        "You're on a dirt road, it has come to an end you can go left or right, which way would you like to go? "
    )
    .strip()
    .lower()
)

if answer == "left":

    answer = (
        input(
            "You come to a river, you can walk around it or swim across, walk or swim?"
        )
        .strip()
        .lower()
    )

    if answer == "swim":
        print("You swam across and were eaton by an alligator.")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")

elif answer == "right":

    answer = (
        input(
            "You come to a bridge, it looks wobbly, do you want to cross it or head back? "
        )
        .strip()
        .lower()
    )

    if answer == "back":
        print("you go back and lose.")

    elif answer == "cross":

        answer = (
            input("you cross the bridge and meet a stranger. Do you talk to them? ")
            .strip()
            .lower()
        )

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")

        elif answer == "no":
            print("You ignore this stranger and they are offended and you lose.")

        else:
            print("Not a valid option. You lose.")

else:
    print("Not a valid option. you lose.")


print(f"Thank you for trying {name}")
