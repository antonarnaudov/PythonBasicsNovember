judges_count = int(input())

presentation = input()
average_sum = 0
presentations_count = 0

while presentation != 'Finish':
    average_score = 0
    for _ in range(judges_count):
        average_score += float(input())

    average_score /= judges_count
    print(f"{presentation} - {average_score:.2f}.")

    average_sum += average_score
    presentations_count += 1
    presentation = input()

average_sum /= presentations_count
print(f"Student's final assessment is {average_sum:.2f}.")
