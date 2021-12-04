age = int(input())
laundry_price = float(input())
toy_price = int(input())

money = 0
toys = 0
amount = 0

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        amount += 10
        money += amount - 1
    else:
        toys += 1

money += toys * toy_price

if money >= laundry_price:
    print(f"Yes! {money - laundry_price:.2f}")
else:
    print(f"No! {laundry_price - money:.2f}")
