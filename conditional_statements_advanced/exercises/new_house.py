flowers_type = input()
flowers_count = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

final_price = 0

if flowers_type == 'Roses':
    final_price = roses_price * flowers_count
    if flowers_count > 80:
        final_price = final_price - final_price * 0.1

elif flowers_type == 'Dahlias':
    final_price = dahlias_price * flowers_count
    if flowers_count > 90:
        final_price = final_price - final_price * 0.15

elif flowers_type == 'Tulips':
    final_price = tulips_price * flowers_count
    if flowers_count > 80:
        final_price = final_price - final_price * 0.15

elif flowers_type == 'Narcissus':
    final_price = narcissus_price * flowers_count
    if flowers_count < 120:
        final_price = final_price + final_price * 0.15

elif flowers_type == 'Gladiolus':
    final_price = gladiolus_price * flowers_count
    if flowers_count < 80:
        final_price = final_price + final_price * 0.2

if budget >= final_price:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - final_price:.2f} leva left.")
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")
