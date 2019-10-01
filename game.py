"""A number-guessing game."""
def checknumber(n):
    while True:
        while n.isdigit() == False:
            print("Invalid, please enter a whole number: ")
            n = input("")
        n = int(n)
        
        if n <1 or n >100:
            print("Out of range, please choose between 1 and 100")
            n = input("")
        else: 
            break
    return n

    
# Put your code here
from random import randint
print("Hello!")
name = input("What is your name? ")
score_log = []
while True:
    print(f"Hi {name}! I'm thinking of a number between 1 and 100. Guess what it is!")

    usernumber = input("")
    secretnumber = randint(1,100)

    count = 0
    while usernumber != secretnumber:
        usernumber = checknumber(usernumber)

        if usernumber > secretnumber:
            print("Too High!")
            usernumber = input("Guess Again! ")

        elif usernumber < secretnumber:
            print("Too Low!")
            usernumber = input("Guess Again! ")
        count += 1

    print(f"That's right! You got it in {count} tries!")
    score_log.append(count)
    print("Do you want to play again? Y/N?")
    answer = input("")
    if answer.upper() == "Y":
        continue
    else:
        best = min(score_log)
        print(f"Your best score was {best}! Goodbye!")
        break

