from prac_08.car import Car
from prac_08.unreliable_car import UnreliableCar


def main():
    junk_heap = UnreliableCar(120, "Junk heap", 64)
    print(junk_heap)
    junk_heap.drive(75)
    print(junk_heap)

main()
