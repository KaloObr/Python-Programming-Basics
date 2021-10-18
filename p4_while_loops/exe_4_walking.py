goal = 10000
current_steps = 0

while current_steps < goal:
    steps_daily = input()
    if steps_daily == "Going home":
        remaining_steps = int(input())
        current_steps += remaining_steps
        break
    current_steps += int(steps_daily)

if current_steps >= goal:
    print("Goal reached! Good job!")
else:
    print(f"{goal - current_steps} more steps to reach goal.")

