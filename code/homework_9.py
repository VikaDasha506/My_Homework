from cities import cities_list
cities_set = set()
flag = True
for cities in cities_list:
    if cities['name'][-1] != 'ь' and cities['name'][-1] != 'й' and cities['name'][-1] != 'ы':
        cities_set.add(cities['name'])
while flag:
    user_city = input('Введите название города:')
    if user_city.lower() == 'стоп':
        flag = False
        print('Вы проиграли!')
        break
    if user_city.title() in cities_set:
        from random import choice
        computer_response = [city for city in cities_set if city[0].lower() == user_city[-1].lower()]
        computer_response = choice(computer_response)
        print(computer_response)
        cities_set.remove(computer_response)
    else:
        flag = False
        print(f'Вы проиграли! "{user_city}" такого города нет, или Вы его уже называли!')
        break







