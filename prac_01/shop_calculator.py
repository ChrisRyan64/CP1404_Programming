number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    number_of_items = int(input("Invalid number of items. Please enter valid value."))
price_total = 0
for i in range(0, number_of_items):
    item_price = int(input("Price of Item: "))
    price_total = price_total + item_price
if price_total > 100:
    price_total = price_total *0.9
print(price_total)