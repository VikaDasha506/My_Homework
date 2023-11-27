from cities import cities_list
from pprint import pprint
import json

# cities_set = set()
# for cities in cities_list:
#    if cities['name'][-1].lower() not in 'ъыь':
#        cities_set.add(cities['name'])
# with open('cities.json', 'w', encoding='UTF-8') as file:
#    json.dump(list(cities_set), file, ensure_ascii=False, indent=4)
flag = True
result = ''
with open('cities.json', 'r', encoding='UTF-8') as file:
    cities_set = json.load(file)
while flag:
    user_city = input('Введите название города:')
    if user_city.lower() == 'стоп':
        flag = False
        result += 'Вы проиграли!'
        break
    if user_city.title() in cities_set:
        from random import choice

        computer_response = [city for city in cities_set if city[0].lower() == user_city[-1].lower()]
        computer_response = choice(computer_response)
        print(computer_response)
        cities_set.remove(computer_response)
    else:
        flag = False
        result += f'Вы проиграли! "{user_city}" такого города нет, или Вы его уже называли!'
        break
else:
    result += 'Вы выиграли!!!'
print(result)
