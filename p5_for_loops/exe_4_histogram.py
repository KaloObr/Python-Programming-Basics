total_numbers = int(input())

p1_stats = 0
p2_stats = 0
p3_stats = 0
p4_stats = 0
p5_stats = 0

for i in range(total_numbers):
    numbers = int(input())

    if numbers <= 199:
        p1_stats += 1
    elif 200 <= numbers <= 399:
        p2_stats += 1
    elif 400 <= numbers <= 599:
        p3_stats += 1
    elif 600 <= numbers <= 799:
        p4_stats += 1
    elif numbers >= 800:
        p5_stats += 1

print(f"{p1_stats / total_numbers * 100:.2f}%")
print(f"{p2_stats / total_numbers * 100:.2f}%")
print(f"{p3_stats / total_numbers * 100:.2f}%")
print(f"{p4_stats / total_numbers * 100:.2f}%")
print(f"{p5_stats / total_numbers * 100:.2f}%")

