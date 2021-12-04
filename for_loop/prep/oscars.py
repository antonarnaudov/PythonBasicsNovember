actor = input()
points = float(input())
judges_count = int(input())

has_oscar = False
points_needed = 1250.5

for judge in range(judges_count):
    judge_name = input()
    judge_points = float(input())

    points += len(judge_name) * judge_points / 2

    if points > points_needed:
        print(f"Congratulations, {actor} got a nominee for leading role with {points:.1f}!")
        has_oscar = True
        break


if not has_oscar:
    print(f"Sorry, {actor} you need {points_needed - points:.1f} more!")
