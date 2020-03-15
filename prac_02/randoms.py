#RANDOM NUMBERS --------------------------------------------------------------------------------------------------------
#TODO: randoms.py (Note: never name a file the same as a module; e.g. random.py or it will have higher precedence when you, e.g. import random)
#In your console, type in the following (run each print line multiple times), and write the answers to the questions below in comments in randoms.py.

import random
print(random.randint(5, 20)) #Smallest number = 5, Largest number = 20. The code can only output random number between 5 and 20.
print(random.randrange(3, 10, 2)) #Smallest number = 3, Largest number = 10. The code can only output 3, 5, 7, 9 as has a step of 2 and cannot be <3 and cannot be >10 in range.
print(random.uniform(2.5, 5.5)) #Smallest number = 2.5, Largest number = 5.5

#TODO: Write code, not a comment, to produce a random number between 1 and 100 inclusive.

import random #imports random numbers
print(random.randint(1, 100)) #prints numbers between 1 and 100 randomly
