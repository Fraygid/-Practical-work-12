import random

random_num = []
for i in range(5):
    random_num.append(random.randint(1, 100))

print(f'Изначальный список: {random_num}')

min_index = 0

for i in range(1, len(random_num)):
    if random_num[i] < random_num[min_index]:
        min_index = i

random_num[0], random_num[min_index] = random_num[min_index], random_num[0]

print(f'Список после обмена: {random_num}')
