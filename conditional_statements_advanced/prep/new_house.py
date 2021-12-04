flower_type = input()
flowers_count = int(input())
budget = int(input())

roses_price = 5
dahlias_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

final_price = 0

if flower_type == 'Roses':
    final_price = flowers_count * roses_price
    if flowers_count > 80:
        final_price -= final_price * 0.1

elif flower_type == 'Dahlias':
    final_price = flowers_count * dahlias_price
    if flowers_count > 90:
        final_price -= final_price * 0.15

elif flower_type == 'Tulips':
    final_price = flowers_count * tulips_price
    if flowers_count > 80:
        final_price -= final_price * 0.15

elif flower_type == 'Narcissus':
    final_price = flowers_count * narcissus_price
    if flowers_count < 120:
        final_price += final_price * 0.15

elif flower_type == 'Gladiolus':
    final_price = flowers_count * gladiolus_price
    if flowers_count < 80:
        final_price += final_price * 0.20

if budget >= final_price:
    print(f'Hey, you have a great garden with {flowers_count} '
          f'{flower_type} and {budget - final_price:.2f} leva left.')
else:
    print(f"Not enough money, you need {final_price - budget:.2f} leva more.")
