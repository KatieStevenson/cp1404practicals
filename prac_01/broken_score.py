"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score > 100:
    print("Invalid score")
elif score > 50:
    print("Passable")
elif score > 90:
    print("Excellent")
elif score < 50:
    print("Bad")

# Changed if statements to ELIF as I would enter a scrore greater than 100.
# It would print "Invalid score", "Passable", "Excellent" and "Bad" etc.
