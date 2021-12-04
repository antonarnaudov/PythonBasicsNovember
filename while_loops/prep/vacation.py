vacation_money = float(input())
money = float(input())

spending_days = 0
days = 0
while True:
    days += 1
    action = input()
    amount = float(input())
    if action == 'spend':
        spending_days += 1
        if spending_days == 5:
            print("You can't save the money.")
            print(f'{days}')
            break
        money -= amount
        if money < 0:
            money = 0
    else:
        money += amount
        spending_days = 0

    if money >= vacation_money:
        print(f"You saved the money for {days} days.")
        break
