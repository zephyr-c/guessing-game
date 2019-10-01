"""A number-guessing game."""

# Put your code here
from random import randint
print("Hello!")
name = input("What is your name? ")
print(f"Hi {name}! I'm thinking of a number between 1 and 100. Guess what it is!")

usernumber = input("")
while usernumber.isdigit() == False:
    print("Invalid input. Please enter a whole number!")
    usernumber = input("")

usernumber = int(usernumber)
secretnumber = 4 #randint(1,100)

count = 1
while usernumber != secretnumber:
    while usernumber < 1 or usernumber > 100:
        print("Invalid input, try again!")
        usernumber = int(input(""))

    if usernumber > secretnumber:
        print("Too High!")
        usernumber = int(input("Guess Again! "))
    elif usernumber < secretnumber:
        print("Too Low!")
        usernumber = int(input("Guess Again!"))
    count += 1

print(f"That's right! You got it in {count} tries!")

