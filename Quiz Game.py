# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------
# ?                                                                     --------1--------
#!--------------------------------------------------------------------      Quiz Game    -------------------------------------------------------------------------
# ?                                                                     --------1---------
# ---------------------------------------------------------------------------Beginner-----------------------------------------------------------------------------


print("Welcome To My Computer Quiz!😁")

playing = input("Do You Want To Play? (y/n) ").lower()

# if playing.lower() not in ["yes", "y"]: # i think the good practice is put .lower in input statement!
if playing not in ["yes", "y"]:
    quit()

print("Ok Lets Play :)")

score = 0
answer = input("What Does AD stand for? ").lower()
if answer == "after death":
    print("Correct!")
    score += 1
else:
    print("Incorrect -_-")


answer = input("What Does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect -_-")


answer = input("What Does PC stand for? ").lower()
if answer == "personal computer":
    print("Correct!")
    score += 1
else:
    print("Incorrect -_-")

# print(f"Congrat. You got {score} quesions corrects")
print(f"Congrat. You got {(score / 3) * 100}%")
