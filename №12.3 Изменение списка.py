users = ['Admin', 'Guest', 'User', 'Bot']

print(f'Изначальный вид списка: {users}')

users[2] = 'Moderator'
users[-1] = 'SuperAdmin'
users.append('NewBie')

print(f'Итоговый список: {users}')
