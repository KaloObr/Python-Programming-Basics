n = int(input())
count = 0
biggest_so_far = 0

while count < n:
    value = int(input())
    if value > biggest_so_far:
        biggest_so_far = value

    count += 1

print(biggest_so_far)