required_money = float(input())
available_money = float(input())
days = 0
days_spending = 0
has_failed = False


while available_money <= required_money:
    action = input()
    current_amount = float(input())

    if action == 'save':
        available_money += current_amount
    else:
        days_spending += 1
        if current_amount > available_money:
            available_money = 0
        else:
            available_money -= current_amount
        if days_spending >= 5:
            has_failed = True
            break

    days += 1


if has_failed:
    print("You can't save the money.")
    print(days_spending)
else:
    print(f"You saved the money for {days} days.")

