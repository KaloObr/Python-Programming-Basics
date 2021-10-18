group_budget = int(input())
season = input()
number_of_fisherman = int(input())

total_cost = 0
discount = 0

if season == "Spring":
    total_cost += 3000
elif season == 'Summer' or season == 'Autumn':
    total_cost += 4200
else:
    total_cost += 2600


if number_of_fisherman <= 6:
    discount = 0.10 * total_cost
elif 7 <= number_of_fisherman <= 11:
    discount = 0.15 * total_cost
else:
    discount = 0.25 * total_cost

if number_of_fisherman % 2 == 0 and season != "Autumn":
    discount += 0.05 * total_cost

final_price = total_cost - discount

if final_price <= group_budget:
    print(f"Yes! You have {group_budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_price - group_budget:.2f} leva.")

