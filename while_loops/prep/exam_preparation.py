max_bad_grades = int(input())

bad_grades = 0
grades_sum = 0
grades_count = 0
last_problem = ''
has_passed = False

while True:
    problem_name = input()
    if problem_name == 'Enough':
        has_passed = True
        break

    grade = int(input())
    if grade <= 4:
        bad_grades += 1
        if bad_grades == max_bad_grades:
            break
    grades_sum += grade
    grades_count += 1
    last_problem = problem_name


if has_passed:
    print(f"Average score: {grades_sum / grades_count:.2f}")
    print(f"Number of problems: {grades_count}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades} poor grades.")
