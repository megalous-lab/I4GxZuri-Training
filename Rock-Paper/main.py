#-----------------------------------------------------------------------------------------------------------------------------------------
import random
opt = ["R", "P", "S"]

print("Welcome to Rock-Paper-Scissors game! \nTo save time, know that R represent Rock, P represent Paper and S represent Scissors \nLet's start!")

# Ask for the user input
user = str(input("Pick an option between R, P and S: ")).upper()
computer = random.choice(opt) # The computer choice

dict = {"R":"Rock", "P":"Paper", "S":"Scissors"}

# Check whether the choosen word is among the list of word
while user not in opt:
    print("Oops! That is not among the list of choice. \n You can only choose 'R', 'P' or 'S'. \n Cheers! You can still choose again!")
    user = str(input("Pick an option between R, P and S: ")).upper()




# Check whether it is a tie!
while user == computer:    
    print("Player ",dict[user],": CPU ",dict[computer]) 
    print("It is a tie! \nPal, This is getting more interesting! \nLet's try again!")
    user = str(input("Pick an option between R, P and S: ")).upper()
    computer = random.choice(opt)

# Determine the winner!
# Print both player's and CPU's move
print("Player ",dict[user],": CPU ",dict[computer])
if (user == "R" and computer == "S") or (user == "P" and computer == "R") or (user == "S" and computer == "P"):
    print("You win!")
else:
    print("Computer wins!")