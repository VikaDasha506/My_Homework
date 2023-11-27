# nums = ['+77053183958','+77773183958','87773183958','+(777)73183958','+7(777)-731-83-58','+7(777) 731 83 58']
#номера для проверки:
# +77053183958;+77773183958;87773183958;+(777)73183958;+7(777)-731-83-58;+7(777) 731 83 58;8705874556;97058745569;870525478932;+789785jh825;8.925.788.5555

phone_number = input('Введите номер телефона через ";" :')
phone_number = (((phone_number.strip().
                  replace(' ', '').
                  replace('-', '').
                  replace('(', '')).
                 replace(')', '')).
                replace('+', '')).split(';')
for number in phone_number:
    try:
        if number[0] != '7':
            if number[0] != '8':
                raise ValueError(f'Номер {number} должен начинаться с "+7" или "8"!')
        if len(number) != 11:
            raise ValueError(f'В номере {number} должно быть "11" цифр!')
        if not(number.isdigit()):
            raise ValueError(f'В номере {number} не должно быть букв и символов!')
    except ValueError as e:
        print(f'Ошибка!Телефон {number} не соответствует формату.{e}!')


data_lst = ['1', '2', '3', '4d', 5, 'd', 'S3d', 'avf', 10, 'ji15']
new_list = []
no_num = []
for elem in data_lst:
    try:
        elem = int(elem)
        new_list += str(elem).split()
    except ValueError:
        no_num += str(elem).split()
if new_list:
    print(f'Данные: {new_list} являются числом')
raise ValueError(f'Данные: {no_num} не являются числом')
