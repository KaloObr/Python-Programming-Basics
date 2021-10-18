name = input()
school_grade = 1
overall_score = 0

while school_grade <= 12:
    grades = float(input())
    if grades < 4:
        continue

    overall_score += grades
    school_grade += 1

final_score = overall_score / 12

print(f"{name} graduated. Average grade: {final_score:.2f}")


