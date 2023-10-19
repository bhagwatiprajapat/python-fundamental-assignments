import random

num=random.randint(1,20)

while True:
    guess=int(input("Grater A Number Between 1 to 20:"))
    if guess==num:
        print("Guess Number A Correct Number")
        break
    elif guess>num:
        print("You Guessed A Gratrer Number")
    elif guess<num:
        print("You Gussed A Smaller Number")
