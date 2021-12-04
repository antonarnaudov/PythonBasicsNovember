screening_type = input()
seat_rows_count = int(input())
seat_cols_count = int(input())

premiere = 12.00
normal = 7.50
discount = 5.00

income = 0
cinema_capacity = seat_rows_count * seat_cols_count

if screening_type == 'Premiere':
    income = cinema_capacity * premiere

elif screening_type == 'Normal':
    income = cinema_capacity * normal

elif screening_type == 'Discount':
    income = cinema_capacity * discount

print(f'{income:.2f} leva')
