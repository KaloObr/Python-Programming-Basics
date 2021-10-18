square_meters = int(input())
price_of_square_meter = 7.61
total_price = square_meters * price_of_square_meter
discounted_price = 0.18 * total_price
final_price = total_price - discounted_price

print(f"The final price is: {final_price:.2f} lv.")
print(f"The discount is: {discounted_price:.2f} lv.")

