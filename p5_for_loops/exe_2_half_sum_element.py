import sys

n = int(input())
max_num = -sys.maxsize
sum_numbers = 0

for i in range(n):
    current_num = int(input())

    if current_num > max_num:
        max_num = current_num

    sum_numbers += current_num

sum_numbers -= max_num

if sum_numbers == max_num:
    print('Yes')
    print(f'Sum = {sum_numbers}')
else:
    print('No')
    print(f'Diff = {abs(max_num - sum_numbers)}')
