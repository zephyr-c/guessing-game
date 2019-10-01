"""A number-guessing game."""
def checknumber(n):
    while n.isdigit() == False:
        print("Invalid input. Please enter a while number!")
        n = input("")
    un = int(n)
    return un 
#def checkrange(x):
 #   while x < 1 or x > 100:
  #      print("Invalid input, try again!")
  #      x = input("")
  #      x = checknumber(x)

    
# Put your code here
from random import randint
print("Hello!")
name = input("What is your name? ")
print(f"Hi {name}! I'm thinking of a number between 1 and 100. Guess what it is!")

usernumber = input("")
secretnumber = 50#randint(1,100)

#print(secretnumber)

count = 1
while usernumber != secretnumber:
    usernumber = checknumber(usernumber)

    if usernumber > secretnumber:
        print("Too High!")
        usernumber = input("Guess Again! ")

    elif usernumber < secretnumber:
        print("Too Low!")
        usernumber = input("Guess Again!")
    count += 1

print(f"That's right! You got it in {count} tries!")

