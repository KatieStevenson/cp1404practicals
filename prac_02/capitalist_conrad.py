"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0

price = INITIAL_PRICE
print("${:,.2f}".format(price))

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("${:,.2f}".format(price))


#TODO (1): The program currently runs without telling us how many days it simulated. Add this feature using a day counter and string formatting so that the program prints like:
    '''
    Starting price: $10.00  
    On day 1 price is: $9.89  
    ...  
    On day 424 price is: $915.71  
    On day 425 price is: $1,001.60
    '''
    import random

    MAX_INCREASE = 0.1  # 10%
    MAX_DECREASE = 0.05  # 5%
    MIN_PRICE = 0.01
    MAX_PRICE = 1000.0
    INITIAL_PRICE = 10.0

    price = INITIAL_PRICE
    day_counter = 0 #adds a counter to determine on what day will the price variable be

    print("The initial price is ${:,.2f}".format(price))

    while price >= MIN_PRICE and price <= MAX_PRICE:
        price_change = 0
        day_counter += 1 #repetitiously adds 1 count per price change

        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print("On day {} price is ${:,.2f}".format(day_counter, price))



#TODO (2): Try changing these so the allowed price range is $1 to $100 and the increase could be up to 17.5% (remember to change any comments that refer to constant values)

    import random

    MAX_INCREASE = 0.175  # 17.5%
    MAX_DECREASE = 0.05  # 5%
    MIN_PRICE = 1.00
    MAX_PRICE = 100.00
    INITIAL_PRICE = 10.0

    price = INITIAL_PRICE
    day_counter = 0 #adds a counter to determine on what day will the price variable be

    print("The initial price is ${:,.2f}".format(price))

    while price >= MIN_PRICE and price <= MAX_PRICE:
        price_change = 0
        day_counter += 1 #repetitiously adds 1 count per price change

        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print("On day {} price is ${:,.2f}".format(day_counter, price))

#TODO (3): Update your program so that it prints (writes) the output to a file.

import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.00
INITIAL_PRICE = 10.0
OUTPUT_FILE = "prac_2_capitalist_conrad_output"

price = INITIAL_PRICE
day_counter = 0 #adds a counter to determine on what day will the price variable be

print("The initial price is ${:,.2f}".format(price))
out_file = open(OUTPUT_FILE, 'w')

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    day_counter += 1 #repetitiously adds 1 count per price change

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} price is ${:,.2f}".format(day_counter, price), file = out_file)

out_file.close()


