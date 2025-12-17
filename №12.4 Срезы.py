data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

first_three = data[:3]
last_three = data[-3:]
reversed = data[::-1]
odd = data[1::2]

print(f'Изначальный вид списка: {data}')
print(f'Первая тройка чисел: {first_three}')
print(f'Последняя тройка чисел: {last_three}')
print(f'Список в обратном порядке: {reversed}')
print(f'Только нечетные индексы: {odd}')
