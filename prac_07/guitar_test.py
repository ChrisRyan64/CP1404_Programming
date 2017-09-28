from prac_07.guitars_class import Guitar


def main():
    example_vintage = Guitar("Gibson", 1922, 16001.95)
    example_other = Guitar("Peasant", 2013, 2100)
    print("Gibson get_age() - Expected 95. Got", example_vintage.get_age())
    print("Peasant get_age() - Expected 4. Got", example_other.get_age())
    print("Gibson is_vintage() - Expected True. Got", example_vintage.is_vintage())
    print("Peasant is_vintage() - Expected False. Got", example_other.is_vintage())


main()