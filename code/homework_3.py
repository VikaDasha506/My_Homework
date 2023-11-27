checking_word = input('Введите слово:')
if checking_word.upper() == (checking_word.upper()[::-1]):
    print(f'Обнаружен палиндром: "{checking_word}"')
else:
    print(f'Слово "{checking_word} "не является палидромом!')
