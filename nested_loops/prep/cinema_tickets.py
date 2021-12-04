movie_name = input()

student_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0
all_tickets_count = 0

while movie_name != 'Finish':
    free_spaces = int(input())
    spaces_taken = 0

    ticket_type = input()
    while ticket_type != 'End':
        all_tickets_count += 1
        spaces_taken += 1
        if ticket_type == 'student':
            student_tickets_count += 1
        elif ticket_type == 'standard':
            standard_tickets_count += 1
        elif ticket_type == 'kid':
            kid_tickets_count += 1

        if free_spaces - spaces_taken == 0:
            break
        ticket_type = input()

    print(f"{movie_name} - {spaces_taken / free_spaces * 100:.2f}% full.")
    movie_name = input()

print(f"Total tickets: {all_tickets_count}")
print(f"{student_tickets_count / all_tickets_count * 100:.2f}% student tickets.")
print(f"{standard_tickets_count / all_tickets_count * 100:.2f}% standard tickets.")
print(f"{kid_tickets_count / all_tickets_count * 100:.2f}% kids tickets.")
