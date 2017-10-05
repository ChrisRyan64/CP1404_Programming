from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "(q)uit, (c)hoose taxi, (d)rive"


def main():
    prius = Taxi(100, "Prius")
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print("Let's Drive!")
    menu_choice = input(MENU.lower())
    while menu_choice != "q":
        if menu_choice == "c" or menu_choice == "d":
            if menu_choice == "c":
                pass
        else:
            print("nope")
        menu_choice = input(MENU.lower())
# Piss off, didn't even click commit, i clicked the arrow

main()
