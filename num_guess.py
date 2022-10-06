#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Sep. 29, 2022
# This program asks for a number
# between 1 and 9, and then tells
# you if your guess was correct


import num_guess_constants


def main():
    # input
    print("This program asks for a number")
    print("between 1 and 9, and then tells")
    print("you if your guess was correct")
    print("")
    user_guess = int(input("Enter a number between 1 and 9: "))

    # process/output
    if user_guess == num_guess_constants.CORRECT_GUESS:
        print("Your guess was correct!")
    else:
        print("Your guess was incorrect.")


if __name__ == "__main__":
    main()
