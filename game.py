"""A number-guessing game."""

import random

computer_num = random.randint(1, 101)
num_user_guesses = 0

print("Howdy, what's your name?")
username = input("> ")

print(f"Welcome to the Number Guessing Game, {username}!")

print(f"{username}, I'm thinking of a number between 1 and 100.")

while True:

    guess_by_user = input("Try to guess the number:  ")
    guess_by_user = int(guess_by_user)

    if guess_by_user < 1 and guess_by_user > 100:
        print(f"Not a valid number for this game.")
        print(f"Please enter a number between 1 and 100")
        continue

    elif guess_by_user < computer_num:
        print(f"Your number is too low.  Please try again.")
        num_user_guesses = num_user_guesses + 1

    elif guess_by_user > computer_num:
        print(f"Your number is too high.  Please try again.")
        num_user_guesses = num_user_guesses + 1
        
    elif guess_by_user == computer_num:
        print(f"Nice work, {username}!")
        print(f"You found the number in {num_user_guesses} tries!")
        break
