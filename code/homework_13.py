from marvel import full_dict
from pprint import pprint

input_number = input('Введите цифры через пробел:').split()


def check_number(num):
    try:
        return int(num)
    except ValueError:
        return None


numbers_int = list(map(check_number, input_number))
result_films_titles = list(filter(lambda movie: movie[0] in numbers_int,
                                  full_dict.items()))
pprint(result_films_titles) # 2. Напишите пользовательский ввод цифр через пробел, разбейте его на список, и примените
# к каждому элементу списка int используя map , но только в том случае, если этот элемент списка число, иначе замените его на None
# 3. Используйте filter и получите аналогичный по структуре словарь, который будет содержать исходные id и
# остальные ключи, но только тех фильмов, id которых есть в полученном списке в п.2

movie_directors = {movie[1]['director'] for movie in full_dict.items()}
pprint(movie_directors) #4. Составьте set comprehension (генератор множества)
# собрав множество содержимого ключа director словаря дата-сета

copy_full_dict_year = {key: {key_: str(value_) if key_ == 'year' else value_ for key_, value_ in value.items()}
                       for key, value in full_dict.items()}
pprint(copy_full_dict_year)# 5. Составьте dict comprehension (генератор словаря) сделав копию исходного словаря full_dict , при этом
# применим в к каждому 'year' значению, функцию str

filter_film_f = dict(filter(lambda movie: movie[1]['title'][0] == 'Ч', full_dict.items()))
pprint(filter_film_f) # 6. Используйте filter и получите аналогичный по структуре словарь, который будет содержать
# исходные id и остальные ключи, но только тех фильмов, которые начинаются на букву Ч

# Cортировка словаря full_dict по 'title'
sorted_full_dict = sorted(full_dict.items(), key=lambda movie: movie[1]['title'])
pprint(sorted_full_dict, sort_dicts=False) #7. Сделайте сортировку словаря full_dict по одному (любому) параметру,
# с использованием lambda на выходе аналогичный по структуре словарь.
# Обязательно подпишите, по какому параметру вы делаете сортировку!

# Cортировка словаря full_dict по 'title','year'
sorted_full_dict2 = sorted(full_dict.items(), key=lambda movie: (movie[1]['title'], movie[1]['year']))
pprint(sorted_full_dict2, sort_dicts=False)# 8. Опционально: сделайте сортировку словаря full_dict
# по двум (любом) параметрам, с использованием lambda на выходе аналогичный по структуре словарь.
# Обязательно подпишите, по какому параметру вы делаете сортировку!

# Отфильтрованный через filter и с использованием в этой же строке sorted по длине 'title'
full_dict_sorted_filtered = sorted((filter(lambda movie: movie[1], full_dict.items())),
                                   key=lambda movie: len(movie[1]['title']))
pprint(full_dict_sorted_filtered, sort_dicts=False)# 9. Опционально: напишите однострочник, в котором мы получаем
# аналогичный по структуре full_dict но отфильтрованный через filter и с использованием в этой же строке sorted
