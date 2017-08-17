''''"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))

# Another (nicer) version of the above loop using the enumerate function
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))

# TODO: Using a for loop with the range function and string formatting,
# produce the following output:
#   0
#  50
# 100

for i in range(0, 3):
    print("Next Number is {:>3}".format(i * 50))'''




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

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "Price_Per_Day.txt"

price = INITIAL_PRICE
day_count = 0
out_file = open(OUTPUT_FILE, "w")
print("Starting price is: ${:,.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    day_count += 1
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("Price for day {0} is: ${1:,.2f}".format(day_count, price), file=out_file)
out_file.close()
if price > MAX_PRICE:
    print("Congratz Conrad")
else:
    print("Suck it, Conrad!")



"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When entering a letter
2. When will a ZeroDivisionError occur? When denominator = 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yep
"""

'''try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        denominator = int(input("Please enter a number other than '0':"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")'''



"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

'''finished = False
result = 0
while not finished:
    try:
        result = int(input("Pick a number:"))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)'''