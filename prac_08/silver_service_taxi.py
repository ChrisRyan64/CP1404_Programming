from prac_08.car import Car
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(fuel, name)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall


    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
