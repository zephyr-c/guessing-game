"""A number-guessing game."""

# Put your code here
from random import randint
print("Hello!")
name = input("What is your name? ")
print(f"Hi {name}! I'm thinking of a number between 1 and 100. Guess what it is!")

usernumber = int(input(""))
secretnumber = 4 #randint(1,100)

while usernumber != secretnumber:
    if usernumber > secretnumber:
        print("Too High!")
        usernumber = int(input("Guess Again! "))
    elif usernumber < secretnumber:
        print("Too Low!")
        usernumber = int(input("Guess Again!"))

print("That's right! You got it in x tries!")

