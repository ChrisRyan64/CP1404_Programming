'''Christopher Ryan'''
def main():
    name = get_name()
    letter_frequency = int(input("Skip how many letters?"))
    while letter_frequency <= 0:
        try:
            letter_frequency = int(input("Enter a value > 0"))
        except ValueError:
            letter_frequency = int(input("Enter a number"))
    display_cut_name(name, letter_frequency)


def display_cut_name(name, skip_frequency):
    for i in range(0, len(name), skip_frequency):
        print(name[i])


def get_name():
    name = input("Enter name: ")
    name_length = len(name)
    while name_length == 0:
        name = input("Invalid name: ")
    return name


main()
