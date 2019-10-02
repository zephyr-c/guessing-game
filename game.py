"""A number-guessing game."""
def isnumber(x):
    while x.isdigit() == False:
        print("Invalid, please enter a whole number: ")
        x = input("")
    x = int(x)
    return x

def checkrange(i):
    while i<1 or i>100:
        print("Out of range, please choose between 1 and 100")
        i = input("")
        i = isnumber(i)
    return i

def checknumber(usernum):
    usernum = isnumber(usernum)
    usernum = checkrange(usernum)
    return usernum

    
# Put your code here
from random import randint
print("Hello!")
name = input("What is your name? ")
score_log = []
while True:
    print(f"Hi {name}! I'm thinking of a number between 1 and 100. Guess what it is!")

    usernumber = input("")
    secretnumber = 50#randint(1,100)

    count = 0
    while usernumber != secretnumber:
        usernumber = checknumber(usernumber)
        count += 1
        remain = 5 - count
        print(f"You have {remain} guesses left!")
        
        if count >5:
            break
        if usernumber == "quit":
            break
        if usernumber > secretnumber:
            print("Too High!")
            usernumber = input("Guess Again! ")

        elif usernumber < secretnumber:
            print("Too Low!")
            usernumber = input("Guess Again! ")
        

    if count >5:
        print("Sorry! Too many guesses!")
    else: 
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

