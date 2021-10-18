budget = float(input())
extras = int(input())
price_per_clothing = float(input())
discount = 0

film_decor = 0.10 * budget
extras_clothes = extras * price_per_clothing

if extras > 150:
    discount = 0.10 * extras_clothes
    extras_clothes -= discount

total_costs = film_decor + extras_clothes

if total_costs > budget:
    print("Not enough money!")
    print(f"Wingard needs {total_costs - budget:.2f} leva more.")
else:
    print('Action!')
    print(f'Wingard starts filming with {budget - total_costs:.2f} leva left.')
