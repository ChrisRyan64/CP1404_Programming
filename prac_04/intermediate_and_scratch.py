import random
from operator import itemgetter

def main():
    '''numbers = []
    for i in range(0, 5):
        number = int(input("Enter a number"))
        numbers.append(number)
    print("The first number is: {}".format(numbers[0]))
    print("The last number is: {}".format(numbers[-1]))
    print("The smallest number is: {}".format(min(numbers)))
    print("The largest number is: {}".format(max(numbers)))
    print("The average is equal to: {}".format(sum(numbers) / len(numbers)))'''

    '''usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_input = input("Enter username: ")
    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")'''

    """
    CP1404/CP5632 Practical
    List comprehensions
    """

    '''names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
    full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
                  "Ada Lovelace"]

    # for loop that creates a new list containing the first letter of each name
    first_initials = []
    for name in names:
        first_initials.append(name[0])
    print(first_initials)

    # list comprehension that does the same thing
    first_initials = [name[0] for name in names]
    print(first_initials)

    # list comprehension that creates a list containing tuples of both initials
    # splits each name and adds the first letter of each part to a tuple
    full_initials = [(name.split()[0][0], name.split()[1][0]) for name in
                     full_names]
    print(full_initials)'''

    '''almost_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(almost_numbers)
    numbers = []
    for almost_number in almost_numbers:
        number = almost_numbers[almost_number]
        numbers.append(number)
    print(numbers)

    # TODO: use a list comprehension to create a list of integers
    # from this list of strings


    # TODO: use a list comprehension to create a list of all of the full_names
    # in lowercase format
    # lowercase_full_names ='''

    # Scratch exercise
    all_picks = []
    total_picks = int(input("How many quick picks?"))
    for i in range(0, total_picks):
        pick_lines = []
        for individual in range(0, 6):
            pick = random.randint(1, 45)
            while pick in pick_lines:
                pick = random.randint(1, 45)
            pick_lines.append(pick)
        pick_lines.sort()
        all_picks.append(pick_lines)
    for p in range(0, total_picks):
        print(all_picks[p])


main()
