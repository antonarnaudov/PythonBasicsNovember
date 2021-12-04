nylon_price = 1.50
paint_price = 14.50
paint_thinner_price = 5.00

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
working_hours = int(input())

nylon_price_sum = (nylon_quantity + 2) * nylon_price
paint_price_sum = (paint_quantity + (paint_quantity * 10 / 100)) * paint_price
paint_thinner_sum = paint_thinner_quantity * paint_thinner_price

supplies_price_sum = nylon_price_sum + paint_price_sum + paint_thinner_sum + 0.40
workers_price = (supplies_price_sum * (30 / 100)) * working_hours

price_sum = supplies_price_sum + workers_price
print(price_sum)
