age= int(input())
washingmachine_price = float(input())
price_per_toy = int(input())

total_saved = 0
number_of_toys = 0
money_per_bday = 0
years_stolen = 0

for i in range(1, age+1):
    if i % 2 == 0:
        money_per_bday += 10
        total_saved += money_per_bday
        years_stolen +=1
    else:
        number_of_toys += 1

total_saved += (number_of_toys * price_per_toy) - years_stolen

if total_saved >= washingmachine_price:
    print(f"Yes! {total_saved - washingmachine_price:.2f}")
else:
    print(f"No! {washingmachine_price - total_saved:.2f}")

