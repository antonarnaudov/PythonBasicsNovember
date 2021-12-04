days_to_stay = int(input())
room_type = input()
assessment = input()

room_price = 18
apartment_price = 25
president_apartment_price = 35

price = 0

if room_type == 'room for one person':
    price = room_price * (days_to_stay - 1)

elif room_type == 'apartment':
    price = apartment_price * (days_to_stay - 1)
    if days_to_stay < 10:
        price -= price * 0.3
    elif days_to_stay <= 15:
        price -= price * 0.35
    else:
        price -= price * 0.5

elif room_type == 'president apartment':
    price = president_apartment_price * (days_to_stay - 1)
    if days_to_stay < 10:
        price -= price * 0.1
    elif days_to_stay <= 15:
        price -= price * 0.15
    else:
        price -= price * 0.2

if assessment == 'positive':
    price += price * 0.25
else:
    price -= price * 0.1

print(f'{price:.2f}')
