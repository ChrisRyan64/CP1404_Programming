print("Electric Bill Simulator")
cents_per_kWh = int(input("Enter cents/kWh: "))
daily_kWh_use = float(input("Enter daily use in kWh: "))
billing_period_days = int(input("Enter number of billing days: "))
total_bill = (cents_per_kWh * daily_kWh_use * billing_period_days) / 100
print("Your estimated bill is: $", total_bill)