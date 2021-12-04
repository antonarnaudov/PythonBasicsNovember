vacation_money = float(input())
money = float(input())

spend_counter = 0
days = 0

while True:
    action = input()
    amount = float(input())
    days += 1
    if action == 'spend':
        spend_counter += 1
        money -= amount
        if money < 0:
            money = 0

        if spend_counter == 5:
            print("You can't save the money.")
            print(f'{days}')
            break
    else:
        money += amount
        spend_counter = 0

    if money >= vacation_money:
        print(f"You saved the money for {days} days.")
        break
