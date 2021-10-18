tabs = int(input())
salary = int(input())
salary_lost = False

for i in range(tabs):
    open_tab = input()

    if salary <= 0:
        salary_lost = True
        break

    if open_tab == 'Facebook':
        salary -= 150
    elif open_tab == 'Instagram':
        salary -= 100
    elif open_tab == 'Reddit':
        salary -= 50


if salary_lost:
    print("You have lost your salary.")
else:
    print(salary)

