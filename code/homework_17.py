from typing import Set
import json


class JsonFile:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def read_file(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def write_file(self, data: set) -> None:
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class Cities:
    """ Этот класс будет использоваться для представления данных о городах из JSON-файла.
        Он будет содержать список всех городов.
    """

    def __init__(self, city_data: set):
        """Принимает список городов city_data. В этом конструкторе происходит наполнение городами."""
        self.city_data = city_data
        self.city_set = self.__get_city_set()

    def __get_city_set(self) -> set:
        city_set = set()
        for city in self.city_data:
            if city[-1].lower() not in 'ъыьй':
                city_set.add(city)
        return city_set


class CityGame:
    """
     Этот класс будет управлять самой игрой.
      Он будет принимать экземпляр класса Cities в качестве аргумента
    """

    def __init__(self, cities: Cities):
        self.cities_obj = cities
        self.cities: Set[set] = self.cities_obj.city_set
        self.human_city: str = ''
        self.computer_city: str = ''

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:
        if last_city[-1].lower() == new_city[0].lower():
            return True
        else:
            return False

    def human_turn(self):
        """ Метод для хода человека,
            который будет обрабатывать ввод пользователя.
        """
        self.human_city = input('Введите город:').title()
        if self.human_city == 'стоп':
            print('Вы проиграли!')
            return False
        if self.human_city.title() not in self.cities:
            print('Такого города нет (или Вы его уже называли)! Вы проиграли!')
            return False
        if self.computer_city:
            if not self.check_game_rules(self.computer_city, self.human_city):
                print(f'Вы проиграли!')
                return False
        self.check_game_over()
        self.cities.remove(self.human_city)
        self.human_city = self.human_city

        return True

    def computer_turn(self):
        """Метод для хода компьютера, который будет выбирать город
         на основе правил игры."""
        for city in self.cities:
            if self.check_game_rules(self.human_city, city):
                print(f'Город компьютера: {city}')
                self.computer_city = city
                self.cities.remove(city)
                return True

        else:
            print('Вы победили!')
            return False

    def check_game_over(self):
        """Метод для проверки завершения игры и определения победителя."""
        if len(self.cities) == 0:
            print('Игра окончена! Вы выиграли!')
        else:
            print('Продолжайте игру!')


class GameManager:
    """Этот класс принимает экземпляры классов JsonFile , Cities и CityGame
    в качестве аргументов
    """

    def __init__(self, json_file: JsonFile, cities: Cities, game: CityGame):
        self.json_file = json_file
        self.cities = cities
        self.game = game

    def __start_game(self):
        """Метод для начала игры, который включает первый ход компьютера"""
        while True:
            if not self.game.human_turn():
                break
            if not self.game.computer_turn():
                break

    def __call__(self):
        self.__start_game()
        print('Игра окончена')
        input('Нажмите Enter для выхода')


if __name__ == '__main__':
    json_file = JsonFile('cities.json')
    cities = Cities(json_file.read_file())
    game = CityGame(cities)
    game_manager = GameManager(json_file, cities, game)
    game_manager()
