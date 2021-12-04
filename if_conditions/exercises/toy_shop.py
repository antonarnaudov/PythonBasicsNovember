tour_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

toys_price = puzzles_count * puzzle_price + talking_dolls_count * talking_doll_price + teddy_bears_count * \
             teddy_bear_price + minions_count * minion_price + trucks_count * truck_price

toys_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

if toys_count >= 50:
    toys_price -= toys_price * 0.25

rent = toys_price * 0.1
income = toys_price - rent

money_left = round(income - tour_price, 2)

if money_left < 0:
    print(f"Not enough money! {abs(money_left):.2f} lv needed.")
else:
    print(f"Yes! {money_left:.2f} lv left.")
