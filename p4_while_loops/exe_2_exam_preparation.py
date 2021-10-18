bad_grades_allowed = int(input())
current_bad_grades = 0
problem_name = input()
overall_score = 0
has_failed = False
number_of_problems = 0
number_of_grade = 0
last_problem = ''

while problem_name != 'Enough':
    grade = int(input())

    if grade <= 4:
        current_bad_grades += 1
        if current_bad_grades == bad_grades_allowed:
            has_failed = True
            break

    number_of_grade += 1
    number_of_problems += 1
    overall_score += grade
    last_problem = problem_name
    problem_name = input()


if has_failed:
    print(f"You need a break, {bad_grades_allowed} poor grades.")
else:
    print(f"Average score: {overall_score / number_of_grade:.2f}")
    print(f"Number of problems: {number_of_problems}")
    print(f"Last problem: {last_problem}")


