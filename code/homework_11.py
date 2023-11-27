from cities import cities_list
import json


#cities_set = set()
#for cities in cities_list:
#   if cities['name'][-1].lower() not in 'ъыьй':
#       cities_set.add(cities['name'])
#with open('cities.json', 'w', encoding='UTF-8') as file:
#   json.dump(list(cities_set), file, ensure_ascii=False, indent=4)
#with open('cities.json', 'r', encoding='UTF-8') as file:
#   cities_set = json.load(file)
def cities_from_json(file_name: str = 'cities.json') -> set:
    """
    Читает json файл и возвращает сет городов
    :param file_name: 'cities.json'
    :return: сет городов
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        cities_set = set(json.load(file))

    return cities_set


def input_user_stop(user_input):
    """
    Проверяем на слово 'стоп'
    :param user_input: ввод пользователя
    :raise ValueError: если ввод слова "стоп"
    :return: None - если все хорошо
    """
    if user_input.lower() == 'стоп':
        raise ValueError('Вы проиграли!')
    else:
        return None


def city_in_set(user_input, all_cities):
    """
    Проверка на вхождение пользовательского ввода города в список городов
    :param user_input: пользовательский ввод города
    :param all_cities: список городов
    :return: None - если все хорошо
    :raise ValueError- если такого города в списке нет
    """
    if user_input.title() in all_cities:
        return None
    else:
        raise ValueError('Такого города нет (или Вы его уже называли)! Вы проиграли!')


def computer_response(computer_input: str, user_input: str) -> bool:
    """
    Проверяет, что первая буква города-компьютера
    равна последней букве города-пользователя
    :param computer_input: слово компьютера
    :param user_input: слово пользователя
    :return: bool
    """
    if computer_input[-1].lower() == user_input[0].lower():
        return True
    else:
        return False


def computer_move(cities_set: set, computer_input: str) -> str | None:
    """
    Возвращаем ответ компьютера
    :param cities_set:сет городов
    :param computer_input:слово компьютера
    :return:выводим ответ компьютера
    """
    for city in cities_set:
        if computer_response(computer_input, city):
            return city
    else:
        return None


def main():
    cities_set = cities_from_json()
    while True:
        user_city = input('Введите название города:').strip()
        computer_city = computer_move(cities_set, user_city)
        cities_set.remove(computer_city)
        try:
            input_user_stop(user_city)
            city_in_set(user_city, cities_set)
            computer_response(user_city, computer_city)
        except ValueError as error:
            print(error)
            break
        print(computer_city)

    else:
        print('Вы выиграли!')


main()
