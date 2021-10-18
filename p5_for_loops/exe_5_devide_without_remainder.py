total_numbers = int(input())
p1_stats = 0
p2_stats = 0
p3_stats = 0

for i in range(total_numbers):
    numbers = int(input())

    if numbers % 2 == 0:
        p1_stats += 1
    if numbers % 3 == 0:
        p2_stats += 1
    if numbers % 4 == 0:
        p3_stats += 1

print(f"{p1_stats / total_numbers * 100:.2f}%")
print(f"{p2_stats / total_numbers * 100:.2f}%")
print(f"{p3_stats / total_numbers * 100:.2f}%")

