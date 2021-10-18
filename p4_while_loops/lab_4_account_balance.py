amount_of_deposits = int(input())
count = 0
total = 0

while count < amount_of_deposits:
    amount = float(input())
    if amount <=0:
        print('Invalid operation!')
        break
    total += amount
    print(f'Increase: {amount:.2f}')
    count += 1

print(f"Total: {total:.2f}")

