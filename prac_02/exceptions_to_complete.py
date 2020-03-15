#INTERMEDIATE EXERCISES
#Problem For You To Fill In The Blanks - Exceptions
#TODO: Let's write a program that gets an integer from the user and does not crash when a non-number is entered.

finished = False
result = 0
while not finished:
    try:
        number = (int(input("Please enter a number: ")))
        if number != ValueError: #Checks to see if the number entered is an integer or not. If integer, it prints the result, otherwise it will throw an error message.
            finished_result = result + number
            print("Valid result is:", finished_result)
            finished = True

    except ValueError:
        print("Please enter a valid integer.")
