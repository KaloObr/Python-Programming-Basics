start = int(input())
end = int(input())
magic_number = int(input())
correct_combination = 0
total_combinations = 0
not_found = True

for x in range(start, end + 1):
    for y in range(start, end + 1):
        total_combinations += 1

        if not_found:
            if x + y == magic_number:
                correct_combination += total_combinations
                print(f"Combination N:{correct_combination} ({x} + {y} = {magic_number})")
                not_found = False
                break

if not_found:
    print(f"{total_combinations} combinations - neither equals {magic_number}")

