#!/usr/bin/env python3
"""Solution to chapter 1, exercise 1: Guessing game"""
import random

def guessing_game():
    """Generate a random integer from 1 to 100.

Ask the user repeatedly to guess the number.
Until they guess correctly, tell them to guess higher or lower.
"""
    name = input("Enter your Name: ")
    print(f"Hello {name}! Welcome to the guessing game!")
    count = 0
    answer = random.randint(1, 10)
    while user_guess := int(input('What is your guess?: ')):
        if user_guess == answer:
            print(f'Right!  The answer is {user_guess}')
            break
        elif user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        else:
            print(f'Your guess of {user_guess} is too high!')
        count += 1
        if count == 3:
            print(f'You have reached the maximum number of guesses. The answer is {answer}')
            break


guessing_game()