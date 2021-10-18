showcase_type = input()
rows = int(input())
collums = int(input())

cost = 0

if showcase_type == "Premiere":
    cost = (rows * collums) * 12.00
elif showcase_type == "Normal":
    cost = rows * collums * 7.50
else:
    cost = rows * collums * 5.00

print(f'{cost:.2f} leva')
