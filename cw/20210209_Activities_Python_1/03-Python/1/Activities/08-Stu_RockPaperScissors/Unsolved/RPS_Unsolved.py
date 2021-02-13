# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == computer_choice:
    print("Tie! rerun.")
elif (user_choice == "r" and computer_choice=="p"):
        print("You chose rock, computer chose paper. You lose.")

elif (user_choice == "s" and computer_choice=="p"):
        print("You chose scissors, computer chose paper. You win!")

elif (user_choice == "p" and computer_choice=="r"):
        print("You chose paper, computer chose rock. You win!")

elif (user_choice == "s" and computer_choice=="r"):
        print("You chose scissors, computer chose rock. You lose.")

elif (user_choice == "r" and computer_choice=="s"):
        print("You chose rock, computer chose scissors. You win!")

elif (user_choice == "p" and computer_choice=="s"):
        print("You chose paper, computer chose scissors. You lose.")


