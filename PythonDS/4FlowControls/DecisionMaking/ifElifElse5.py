# Calculate Road tax

bike_price = int(input("Enter price of the bike: "))

if (bike_price > 100000):
    tax_amount = bike_price * 15 / 100
elif (bike_price >= 50000):
    tax_amount = bike_price * 10 / 100
else:
    tax_amount = bike_price * 5 / 100

print("Tax amount:", round(tax_amount))
