from prac_08.car import Car
from prac_08.taxi import Taxi


def main():
    test_taxi = Taxi(100, "Prius 1")
    print(test_taxi)
    test_taxi.drive(40)
    print(test_taxi)
    print(test_taxi.get_fare())
    test_taxi.start_fare()
    test_taxi.add_fuel(150)
    print(test_taxi)
    test_taxi.drive(100)
    print(test_taxi.get_fare(), test_taxi, sep=': ')



main()