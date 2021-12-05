judges_count = int(input())

presentation_name = input()
average_score_sum = 0
presentations_count = 0

while presentation_name != 'Finish':
    average_score = 0

    for _ in range(judges_count):
        average_score += float(input())

    average_score /= judges_count
    print(f"{presentation_name} - {average_score:.2f}.")
    average_score_sum += average_score
    presentations_count += 1

    presentation_name = input()

average_score_sum /= presentations_count
print(f"Student's final assessment is {average_score_sum:.2f}.")
