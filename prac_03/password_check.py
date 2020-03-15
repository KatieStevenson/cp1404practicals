'''
On paper, write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet
a minimum length set by a variable.The program should then print asterisks as long as the word.
Example: if the user enters "Pythonista" (10 characters), the program should print "**********".
'''


def main():
    print("Please enter a 8 character password: ")
    password = input("> ")
    return valid_length(password)


def valid_length(password):
    password_length = len(password)
    min_length = 8
    if min_length > password_length:
        print("The password entered is invalid")
        return main()
    else:
        return convert_to_asterisk(password)


def convert_to_asterisk(password):
    print("Your password is: ")
    for char in password:
        print(char.replace(char, '*'), end='')


main()
