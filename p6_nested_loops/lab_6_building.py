total_floor = int(input())
rooms_per_floor = int(input())
floor_print = ''

for floor in range(total_floor, 0, -1):

    for room in range(0, rooms_per_floor):

        if floor == total_floor:
            floor_print += f"L{floor}{room} "

        elif floor % 2 == 0 :
            floor_print += f"O{floor}{room} "

        else:
            floor_print += f"A{floor}{room} "

    print(floor_print)
    floor_print = ''
