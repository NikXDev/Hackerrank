meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

tip = meal_cost * (tip_percent / 100)
tax = meal_cost * (tax_percent / 100)
total_cost = int(round(meal_cost + tip + tax))
print(total_cost)
