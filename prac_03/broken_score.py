"""
Should ask the user for their score and print the result.
Write a new function that takes in the user's score as a parameter and returns the result to be printed.
The function should not print it.
"""


def main():
    score = float(input("Enter score: "))
    print(determine_score(score))


def determine_score(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif score > 50:
        return "Passable"
    elif score > 90:
        return "Excellent"
    elif score < 50:
        return "Bad"


main()
