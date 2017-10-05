from prac_08.car import Car
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    limo = SilverServiceTaxi("Limo", 200, 2)
    print(limo)
    limo.drive(18)
    print(limo)
    print(limo.get_fare())


main()