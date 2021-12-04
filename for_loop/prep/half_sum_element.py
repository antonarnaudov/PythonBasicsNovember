import sys

n = int(input())

max_num = -sys.maxsize
sum_nums = 0

for i in range(0, n):
    num = int(input())

    if max_num < num:
        max_num = num

    sum_nums += num

other_nums = sum_nums - max_num

if max_num == other_nums:
    print('Yes')
    print(f'Sum = {abs(other_nums)}')
else:
    print('No')
    print(f'Diff = {abs(max_num - other_nums)}')
