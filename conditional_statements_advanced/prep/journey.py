budget = float(input())
season = input()

destination = ''
place = ''
expenses = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.30
    elif season == 'winter':
        expenses = budget * 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        expenses = budget * 0.40
    elif season == 'winter':
        expenses = budget * 0.80
else:
    destination = 'Europe'
    expenses = budget * 0.90

if destination == 'Europe':
    place = 'Hotel'
elif season == 'summer':
    place = 'Camp'
elif season == 'winter':
    place = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{place} - {expenses:.2f}')
