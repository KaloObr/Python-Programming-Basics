film = input()
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
total_tickets = 0
total_per_movie = 0

while film != "Finish":
    available_seats = int(input())
    ticket_type = input()

    while ticket_type != "End":
        total_tickets += 1
        total_per_movie += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        if total_per_movie >= available_seats:
            break

        ticket_type = input()

    seats_percent = total_per_movie / available_seats * 100
    print(f"{film} - {seats_percent:.2f}% full.")

    total_per_movie = 0
    film = input()


student_percent = student_tickets / total_tickets * 100
standard_percent = standard_tickets / total_tickets * 100
kid_percent = kid_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
