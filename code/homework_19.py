import json
from dataclasses import dataclass
from jsonschema import validate, ValidationError
from typing import List

city_schema = {
    "type": "object",
    "properties": {
        "coords": {
            "lat": {"type": "string"},
            "lon": {"type": "string"}
        },
        "name": {"type": "string"},
        "population": {"type": "integer"},
        "subject": {"type": "string"},
        "district": {"type": "string"},
    },
    "required": ["name", "population", "subject", "district", "coords"]
}


@dataclass
class City:
    name: str
    population: int
    subject: str
    district: str
    latitude: float
    longitude: float
    is_used: bool = False

    def __eq__(self, other):
        if isinstance(other, City):
            return self.name == other.name
        return False


class Validator:
    def __init__(self, json_schema):
        self.json_schema = json_schema

    def validate(self, data):
        try:
            validate(data, self.json_schema)
        except ValidationError:
            return False
        return True


class Serializer:
    def __init__(self, json_schema):
        self.__validator = Validator(json_schema)

    def __call__(self, city_data: dict) -> City:
        self.__validator.validate(city_data)
        return City(**city_data)

    @staticmethod
    def serialize(city_data):
        return json.dumps(city_data)

    @staticmethod
    def deserialize(json_data) -> City:
        return City(**json.loads(json_data))

    @staticmethod
    def validate_city_data(city_data, json_schema):
        try:
            validate(city_data, json_schema)
        except ValidationError as e:
            raise ValueError(f'Данные города "{city_data["name"]}" не соответствуют схеме. Ошибка: {e}') from e


class JsonFile:
    def __init__(self, filepath, validator: Validator):
        self.filepath = filepath
        self.validator = validator

    def read_file(self):
        with open(self.filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def write_file(self, data: set) -> None:
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def validate_data(validator):
        return validator.validate_data

    def __call__(self, validator, city_data):
        return self.validate_data(city_data, validator)


class Cities:
    def __init__(self, city_data, serializer: Serializer):
        self.city_data = city_data
        self.serializer = serializer
        self.cities_obj_list = self.__get_cities_list()

    def __get_cities_list(self) -> dict:
        cities_obj_list = []
        for city in self.city_data:
            if city['name'][-1].lower() not in 'ъыьй':
                cities_obj_list.append(City(
                    name=city['name'],
                    population=city['population'],
                    subject=city['subject'],
                    district=city['district'],
                    latitude=float(city['coords']['lon']),
                    longitude=float(city['coords']['lon']))
                )
        return cities_obj_list


class CityGame:
    def __init__(self, cities: Cities):
        self.cities_obj = cities
        self.cities: list[City] = self.cities_obj.cities_obj_list
        self.human_city: City | None = None
        self.computer_city: City | None = None

    @staticmethod
    def check_game_rules(last_city: str, new_city: str) -> bool:
        if last_city[-1].lower() == new_city[0].lower():
            return True
        else:
            return False

    def human_turn(self):
        self.human_city = input('Введите город:').title()
        if self.human_city == 'Стоп':
            print('Вы проиграли!')
            return False

        for city in self.cities:
            if city.name == self.human_city:
                if city.is_used:
                    print(f'Город {self.human_city} уже был использован! Вы проиграли!')
                    return False
                else:
                    self.human_city = city
                    break
        else:
            print(f'{self.human_city}: Нет такого города в списке')
            return False

        if self.computer_city:
            if not self.check_game_rules(self.computer_city.name, self.human_city.name):
                print(f'Вы проиграли!')
                return False

        for city in self.cities:
            if city.name == self.human_city:
                city.is_used = True
                break

        self.human_city.is_used = True
        return True

    def computer_turn(self):
        for city in self.cities:
            if self.check_game_rules(self.human_city.name, city.name):
                if city.is_used:
                    continue
                print(f'Город компьютера: {city.name}')
                self.computer_city = city
                city.is_used = True
                return True
        else:
            print('Вы победили!')
            return False

    def check_game_over(self):
        if len(self.cities) == 0:
            print('Игра окончена! Вы выиграли!')


class GameManager:
    def __init__(self, json_file: JsonFile, cities: Cities, game: CityGame):
        self.json_file = json_file
        self.cities = cities
        self.game = game

    def __start_game(self):
        while True:
            if not self.game.human_turn():
                break
            if not self.game.computer_turn():
                break

    def __call__(self):
        self.__start_game()
        print('Игра окончена')


if __name__ == '__main__':
    validator = Validator(city_schema)
    serializer = Serializer(city_schema)
    json_file = JsonFile('cities.json', validator)
    cities = Cities(json_file.read_file(), serializer)
    for city in json_file.read_file():
        try:
            validate(city, city_schema)
        except ValidationError as e:
            print(f'Данные города "{city["name"]}" не соответствуют схеме. Ошибка: {e}')
    game = CityGame(cities)
    game_manager = GameManager(json_file, cities, game)
    game_manager()
