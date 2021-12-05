# num = 5
# text = 'abc'
# number2 = 2
# number3 = 3
# number4 = 4
# number5 = 5
# number6 = 6
#
# if num == 5:
#     num += 2
#     if num == 6 or text == 'abc' and number2 == 2 \
#             and number3 == 3 and number4 == 4 \
#             and number5 == 5 and number6 == 6:
#         print(num, text)
#     else:
#         print('nope')
# else:
#     pass
#

# n = int(input())
# all_names = ''
# for _ in range(n):
#     name = input()
#     if name != 'pesho':
#         all_names += name + ' '
# print(all_names)


command = input()

while command != "End":
    destination = command
    budget = float(input())
    collected_money = 0
    while collected_money < budget:
        current_sum = float(input())
        collected_money += current_sum
    print(f"Going to {destination}!")

    command = str(input())
    if command.isdigit():
        while command.isdigit():
            command = input()
