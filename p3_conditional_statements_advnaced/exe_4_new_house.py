flower_type = input()
flower_quontity = int(input())
budget = int(input())

final_price = 0

if flower_type == 'Roses':
    final_price += flower_quontity * 5
    if flower_quontity > 80:
        discount = 0.10 * final_price
        final_price -= discount
elif flower_type == 'Dahlias':
    final_price += flower_quontity * 3.80
    if flower_quontity > 90:
        discount = 0.15 * final_price
        final_price -= discount
elif flower_type == 'Tulips':
    final_price += flower_quontity * 2.80
    if flower_quontity > 80:
        discount = 0.15 * final_price
        final_price -= discount
elif flower_type == 'Narcissus':
    final_price += flower_quontity * 3
    if flower_quontity < 120:
        extra = 0.15 * final_price
        final_price += extra
else:
    final_price += flower_quontity * 2.50
    if flower_quontity < 80:
        extra = 0.20 * final_price
        final_price += extra

if final_price <= budget:
    print(f"Hey, you have a great garden with {flower_quontity} {flower_type} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")
