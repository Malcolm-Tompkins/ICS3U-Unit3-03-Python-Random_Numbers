#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 4, 2021
# Guess the number game with randomly generated numbers

import random


# Function that runs Guess the number game
def main():
    # User input
    print("Welcome to Guess the number!\nPick a number from 0-100")
    user_number = int(input("\nYour number is: "))
    # Process
    program_number = random.randint(0, 100)
    if user_number == program_number:
        # Output
        print("\nYou have guessed the correct number, nice!")
    else:
        print("\nYou have guessed incorrectly.")
        print("\nThe correct answer was: {}".format(program_number))


if __name__ == "__main__":
    main()
