word = input('Введите слово: ')

chars = list(word)

reversed = chars[::-1]

if chars == reversed:
    print('Слово является палидромом.')
else:
    print('Слово не является палидромом.')
