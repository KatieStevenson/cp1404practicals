"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    password_length = (len(password)) #determines the length of the password entered by user
    if password_length < MIN_LENGTH or password_length > MAX_LENGTH:
        print(False)

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    # TODO: count each kind of character (use str methods like isdigit)
    #assesses what user has inputed for password and then determines the number of digits entered, number of upper and lowercase characters and number of special characters.
    for char in password:
        if char.isdigit(): #checks if any characters have been entered by the user and then counts them
            count_digit += 1
        if char.islower(): #checks if any of the characters are lowercase and counts them
            count_lower += 1
        if char.isupper(): #checks if any of the characters are uppercase and then counts them
            count_upper += 1
        if char in SPECIAL_CHARACTERS: #checks if any characters are considered special characters (as listed under variable SPECIAL_CHARACTERS and then counts them
            count_special += 1

    # TODO: if any of the 'normal' counts are zero, return False
    #normal counts are count_lower, count_upper and count_digit, as count_special (special characters) are not mandatory
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        print(False)

    # TODO: if special characters are required, then check the count of those
    if count_special != 0: #if the count for special characters is not equal to 0 then it will print the total number of special characters, otherwise it will print False.
       print(count_special)
    else:
        print(False)

    return True

main()