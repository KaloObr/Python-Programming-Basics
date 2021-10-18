savings = 0
destination = input()

while destination != "End":
    budget = int(input())

    while budget > savings:
        saved_so_far = int(input())
        savings += saved_so_far

    print(f"Going to {destination}!")
    savings = 0

    destination = input()

