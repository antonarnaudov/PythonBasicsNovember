first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    is_valid = True
    for digit in str(number):
        if int(digit) % 2 == 0:
            is_valid = False

    if is_valid:
        print(number, end=' ')
