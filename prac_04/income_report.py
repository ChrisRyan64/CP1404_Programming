def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    # numbers[0] = "ten"
    # numbers[-1] = 1
    # print(numbers[1:-1])
    '''if 9 in numbers:
        print("Yes")
    else:
        print("No")'''


    month_loop_counter = 1
    total_months = int(input("How many months? "))
    months_income = []
    for month in range(0, total_months):
        monthly_income = int(input("Enter income for month {}:".format(month + 1)))
        months_income.append(monthly_income)
        month_loop_counter += 1
    display_report(total_months, months_income)


def display_report(total_months, months_income):
    total_income = 0
    print("\nIncome Report\n----------")
    for month in range(1, total_months + 1):
        income = months_income[month - 1]
        total_income += income
        print("Month {:2} - Income: ${:8.2f} Total: ${:8.2f}".format(month, income, total_income))


"""
# CP1404/CP5632 Practical
# Starter code for cumulative total income program



def main():
    # Display income report for incomes over a given number of months.
    incomes = []
    months = int(input("How many months? "))

    for month in range(1, months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))"""


main()
