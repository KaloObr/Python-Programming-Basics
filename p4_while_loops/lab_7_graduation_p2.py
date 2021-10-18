name = input()
school_grade = 1
overall_score = 0
failed_once = False

while school_grade <= 12:
    grades = float(input())
    if grades < 4:
        overall_score += grades
        failed_once = True
        if failed_once:
            break

    overall_score += grades
    school_grade += 1


if failed_once:
    print(f"{name} has been excluded at {school_grade} grade")
else:
    final_score = overall_score / 12
    print(f"{name} graduated. Average grade: {final_score:.2f}")

