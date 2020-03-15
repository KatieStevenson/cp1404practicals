#EXCEPTIONS ------------------------------------------------------------------------------------------------------------
#TODO: Run this code, then answer the questions below in comments...

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#Questions
#When will a ValueError occur? - When the numerator and/or denominator are not valid numbers i.e. user enters them as a string
#When will a ZeroDivisionError occur? When user attempts to divide something by zero.
#Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, by accepting the ZeroDivisionError and continue to request user to input a valid response.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)

except ZeroDivisionError: #Wanted to make a function for the below, but had issues with trying to create a function within an exception, this is why I ended up re-using retry_denominator outside and inside the while loop.
    print("Cannot divide by zero!")
    retry_denominator = (int(input("Enter a denominator with a value greater than 0: "))) #allows user to re-enter denominator
    while retry_denominator == 0: #repeatedly checks if user input is greater than 0 and recalculates fraction when a valid number has been provided
        retry_denominator = (int(input("Enter a denominator with a value greater than 0: ")))
    else:
        new_fraction = numerator / retry_denominator
        print(numerator, "/", retry_denominator, "=", new_fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
