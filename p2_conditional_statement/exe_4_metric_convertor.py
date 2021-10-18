number = float(input())
input_metric = input()
output_metric = input()
number_in_meter = 0

if input_metric == 'mm':
    number /= 1000

elif input_metric == 'cm':
    number /= 100

if output_metric == 'cm':
    print(f'{number * 100:.3f}')
elif output_metric == 'mm':
    print(f'{number * 1000:.3f}')
else:
    print(f'{number:.3f}')