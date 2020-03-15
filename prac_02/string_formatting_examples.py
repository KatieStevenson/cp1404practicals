#STRING FORMATTING -----------------------------------------------------------------------------------------------------
# TODO (1): Use string formatting to produce the output: "1922 Gibson L-5 CES for about $16,035!". (Notice where the values go and also the float formatting / number of decimal places.)

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

print("{} {} for about ${:,.2f}!".format(year, name, cost))


# TODO (2): Using a for loop with the range function and string formatting (do not use a list), produce the following output (right-aligned numbers): 0, 50, 100, 150
numbers = [0, 50, 100, 150]

for numbers in numbers:
    print("{:>3}".format(numbers))



















