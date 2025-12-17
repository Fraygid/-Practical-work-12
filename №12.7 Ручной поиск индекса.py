numbers = [10, 20, 30, 40, 50]
found_num = -1

search_num = int(input('Введите число для поиска: '))

for i in range(len(numbers)):
    if numbers[i] == search_num:
        found_num = i
        break

if found_num != -1:
    print(f'Число {search_num} найдено в списке на позиции {found_num}.')
else:
    print(f'Число {search_num} не найдено в списке.')
