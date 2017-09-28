from prac_07.guitars_class import Guitar


def main():
    guitars = []
    continue_flag = True
    while continue_flag:
        guitar_name = input("Enter guitar name")
        if guitar_name == '':
            continue_flag = False
        guitar_year = int(input("Enter guitar year"))
        if guitar_year == '':
            continue_flag = False
        guitar_cost = float(input("Enter guitar cost"))
        if guitar_cost == '':
            continue_flag = False
        if continue_flag:
            guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    for i, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_status = "(vintage)"
        else:
            vintage_status = ''
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage_status))

main()