marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]

count_fives = 0
count_twos = 0

for i in marks:
    if i == 5:
        count_fives += 1
    elif i == 2:
        count_twos += 1

print(f'Количество пятерок: {count_fives}')
print(f'Количество двоек: {count_twos}')
