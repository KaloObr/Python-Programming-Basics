cake_lengh = int(input())
cake_width = int(input())
cake_size = cake_lengh * cake_width

total_pieces = 0

while total_pieces < cake_size:
    current_pieces = input()
    if current_pieces == "STOP":
        break
    total_pieces += int(current_pieces)

if total_pieces > cake_size:
    print(f"No more cake left! You need {total_pieces - cake_size} pieces more.")
else:
    print(f"{cake_size - total_pieces} pieces are left.")

