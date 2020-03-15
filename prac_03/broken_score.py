"""
Should ask the user for their score and print the result.
Write a new function that takes in the user's score as a parameter and returns the result to be printed.
The function should not print it.
"""

import random


def generate_random_number():
    score = random.randint(0, 100)
    return score, determine_score(score)


def determine_score(score):
    if score < 0:
        return "Invalid Score"
    elif score > 100:
        return "Invalid Score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    elif score < 50:
        return "Bad"


def main():
    # score = float(input("Enter score: ")) # COMMENT THIS OUT AS RANDOM NUMBER IS REPLACING USER INPUT

    print(generate_random_number())


main()
