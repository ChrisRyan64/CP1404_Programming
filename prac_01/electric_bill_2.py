print("Electric Bill Simulator")
TARIFF_64 = 0.255543
TARIFF_32 = 0.345678
cents_per_kWh = int(input("Which Tariff? 64 or 32?"))
if cents_per_kWh != 64 and cents_per_kWh != 32:
    print("you suck")
else:
    daily_kWh_use = float(input("Enter daily use in kWh: "))
    billing_period_days = int(input("Enter number of billing days: "))
    total_bill = (cents_per_kWh * daily_kWh_use * billing_period_days) / 100
    print("Your estimated bill is: $", total_bill)