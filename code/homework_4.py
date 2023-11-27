# Задача №1
phone_number = input('Введите номер телефона:')
phone_number = phone_number.strip()
phone_number = phone_number.replace(' ', '').replace('-', '')
checking_for_plus = False  # проверка на плюс
checking_for_parentheses = False  # проверка на скобки
checking_for_length = False  # проверка на длину
password_checking = False  # проверка пароля
password_dash = False  # проверка тире
result = ''
if phone_number.count('+') == 1 or phone_number.find('+') == 0:
    checking_for_plus = True
    phone_number = phone_number.replace('+', '')
if ((phone_number.count('(') == 1 and phone_number.count(')') == 1
     and phone_number.find('(') < phone_number.find(')'))
        or (phone_number.count('(') == 0 and phone_number.count(')') == 0)):
    checking_for_parentheses = True
    phone_number = phone_number.replace('(', '').replace(')', '')
if checking_for_plus:
    if phone_number[0] == '7':
        password_checking = True
    else:
        result += f'Номер должен начинаться на 8 или+7!\n'
else:
    if phone_number[0] == '8':
        password_checking = True
    else:
        result += f'Номер должен начинаться на 8 или +7!\n'
if len(phone_number) == 11:
    checking_for_length = True
else:
    result += f'Длина номера телефона должна быть не меньше 11 знаков!\n'
if checking_for_parentheses and password_checking and checking_for_length:
    result += f'Верный формат ввода телефона!'
else:
    result += f'НЕ верный формат ввода телефона!'
print(result)

# Задача №2
checking_symbol = False
checking_whitespace = False
length_password = False
correct_letter = False
correct_password = False
result = ''

password = input('Введите пароль:')
if ' ' in password:
    correct_password = True
    result += f'\nВ пароле не должно быть пробела!'
    print('проверка на пробел')
else:
    if not (password.isalnum()):
        checking_symbol = True
    else:
        result += f'\nВ пароле отсутствует спецзнак!'
        print('проверка на знак')
    if not (password.isupper() or password.islower()):
        correct_letter = True
    else:
        result += f'В пароле должны содержаться буквы разного регистра!\n'
        print('проверка на буквы')
    if len(password) > 7:
        length_password = True
    else:
        result += f'Пароль должен  быть более 7 символов длиной!\n'
        print('проверка на длину')
if checking_symbol and correct_letter and length_password:
    result += f'Пароль надёжный!'
else:
    result += f'Пароль НЕ надежный!'
print(result)
