n = int(input())
larges_so_far = None
smalles_so_far = None

for i in range(n):
    number = int(input())

    if larges_so_far is None:
        larges_so_far = number
    elif smalles_so_far is None:
        smalles_so_far = number
    elif number < smalles_so_far:
        smalles_so_far = number
    elif number > larges_so_far:
        larges_so_far = number

print(f"Max number: {larges_so_far}")
print(f"Min number: {smalles_so_far}")

