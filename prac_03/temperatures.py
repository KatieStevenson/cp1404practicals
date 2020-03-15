"""
temperatures.py - use 2 functions for converting Celsius to Fahrenheit and vice versa
Important: Remember SRP - functions should do one thing, so these should be calculation functions.
Do not get user input or print output in the functions - do those outside.
That means these will be very small functions... that's OK... they abstract a core piece of functionality.
"""


def calculate_celcius(celcius):
    fahrenheit = celcius * 9.0 / 5 + 32
    return fahrenheit


def calculate_fahrenheit(get_fahrenheit):
    convert_fahrenheit = 5 / 9 * (get_fahrenheit - 32)
    return convert_fahrenheit


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit   """
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        print ("Result: {:.2f} F".format(calculate_celcius(celsius)))

    elif choice == "F":
        get_fahrenheit = float(input("Enter Fahrenheit: "))
        print("Result: {:.2f} C".format(calculate_fahrenheit(get_fahrenheit)))

    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")
