goal = 10000
steps_sum = 0
while True:
    steps = input()
    if steps == 'Going home':
        steps = int(input())
        steps_sum += int(steps)

        if steps_sum >= goal:
            print("Goal reached! Good job!")
            print(f"{steps_sum - goal} steps over the goal!")
        else:
            print(f"{goal - steps_sum} more steps to reach goal.")
        break
    else:
        steps_sum += int(steps)

    if steps_sum >= goal:
        print("Goal reached! Good job!")
        print(f"{steps_sum - goal} steps over the goal!")
        break
