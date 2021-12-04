film_type = input()
rows = int(input())
cols = int(input())

premiere_ticket = 12
normal_ticket = 7.50
discount_ticket = 5

full_capacity = rows * cols
final_price = 0

if film_type == 'Premiere':
    final_price = full_capacity * premiere_ticket
elif film_type == 'Normal':
    final_price = full_capacity * normal_ticket
elif film_type == 'Discount':
    final_price = full_capacity * discount_ticket

print(f'{final_price:.2f} leva')
