from pprint import pprint
from marvel import full_dict

stage = {
    1: "Первая фаза",
    2: "Вторая фаза",
    3: "Третья фаза",
    4: "Четвёртая фаза",
    5: "Пятая фаза",
    6: "Шестая фаза"
}
result = []
number_phase = input('Введите номер фазы:')
if not(number_phase.isdigit()):
    raise TypeError(f'Недопустимый ввод: "{number_phase}"! Введите цифру!')
if number_phase > '6':
    raise ValueError(f'Введенная Вами фаза: "{number_phase}" не существует!')
for key, value in stage.items():
    for key_film, value_film in full_dict.items():
        if int(number_phase) == int(key) and value == value_film['stage']:
            result.append({value: {value_film['title'], value_film['year']}})
pprint(result)
