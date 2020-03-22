'''
WARM UP
Create a Python file called lists_warmup.py and enter the following line:


numbers = [3, 1, 4, 1, 5, 9, 2]

# What values do the following expressions have?
numbers[0] # Lists the very first number = 3
numbers[-1] # Lists the very last number = 2
numbers[3] # Provides the location of number 3 in the list, which is the first number
numbers[:-1] # '-1' = 2 in the list ':' = split, therefore shows the list of numbers but excludes the last number which is 2
numbers[3:4] # Shows the number in between the number 3 and the number 4
5 in numbers # Asks if there is a number 5 in the list of numbers. I am assuming this is TRUE
7 in numbers # Asks if there is a number 7 in the list of numbers. I am assuming this is FALSE
"3" in numbers # Seeing if the string "3" is in the list of numbers. I am assuming this is FALSE or will throw a ValueError
numbers + [6, 5, 3] # Printsthe numbers 6, 5, 3 on the end of the numbers lists, would not modify the list though as no .append method used


'''

# 1) Change the first element of numbers to "ten" (the string, not the number 10)

#   numbers = ["ten", 1, 4, 1, 5, 2]

# 2) Change the last element of numbers to 1

#   numbers = [3, 1, 4, 1, 5, 9, 1]

# 3) Get all the elements from numbers except the first two (slice)
#    numbers = [3, 1, 4, 1, 5, 9, 2]
#    numbers[2:7]

# 4) Check if 9 is an element of numbers
#   9 in numbers = TRUE
