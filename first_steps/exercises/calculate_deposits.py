deposited_amount = float(input())
pay_time = int(input())
annual_interest = float(input())

result = deposited_amount + pay_time * ((deposited_amount * annual_interest / 100) / 12)
print(result)
