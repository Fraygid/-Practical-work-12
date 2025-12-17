num = int(input('Введите число: '))

odd_num = []

for i in range(1, num + 1):
    if i % 2 == 1:
        odd_num.append(i)

print(f'нечетные числа от 1 до {num}: {odd_num}')
