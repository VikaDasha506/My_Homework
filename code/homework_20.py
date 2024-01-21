import requests
from marshmallow import Schema, fields, post_load, INCLUDE
import json
from dataclasses import dataclass, field
from pprint import pprint
from marshmallow.validate import Range


class OpenWeatherMap:
    def __init__(self, city_name):
        self.city_name = city_name

    def get_weather(self):
        api_key = "3256d8d43b81d30651ab5c5390b355b7"
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': self.city_name,
            'lang': 'ru',
            'units': 'metric',
            'appid': api_key
        }
        response = requests.get(base_url, params=params)
        return response.json()


class InputCity:
    def __init__(self):
        self.city_name = input('Введите название города:')


@dataclass
class CurrentWeather:
    coord: dict
    name: str
    main: dict
    weather: list = field(default_factory=list)
    base: str = ""
    visibility: int = 0
    wind: dict = field(default_factory=dict)
    clouds: dict = field(default_factory=dict)
    dt: int = 0
    sys: dict = field(default_factory=dict)
    timezone: int = 0
    id: int = 0
    cod: int = 0


class WeatherSchema(Schema):
    coord = fields.Dict(lon=fields.Float(validate=Range(min=-180, max=180)),
                        lat=fields.Float(validate=Range(min=-90, max=90)))
    weather = fields.List(fields.Dict(id=fields.Int(),
                                      main=fields.Str(), description=fields.Str(), icon=fields.Str()))
    base = fields.Str()
    main = fields.Dict(temp=fields.Float(), feels_like=fields.Float(),
                       temp_min=fields.Float(), temp_max=fields.Float(),
                       pressure=fields.Int(), humidity=fields.Int(validate=lambda value: value >= 0,
                                                                  error_messages={
                                                                      "validate": "Не может быть отрицательной"}),
                       sea_level=fields.Int(), grnd_level=fields.Int())
    visibility = fields.Int()
    wind = fields.Dict(speed=fields.Float(), deg=fields.Int(), gust=fields.Float())
    clouds = fields.Dict(all=fields.Int())
    dt = fields.Int()
    sys = fields.Dict(type=fields.Int(), id=fields.Int(), country=fields.Str(),
                      sunrise=fields.Int(), sunset=fields.Int())
    timezone = fields.Int()
    id = fields.Int()
    name = fields.Str()
    cod = fields.Int()

    @post_load
    def make_weather(self, data) -> CurrentWeather:
        return CurrentWeather(**data)


if __name__ == '__main__':
    city = InputCity()
    weather_schema = OpenWeatherMap(city.city_name).get_weather()
    city_weather = WeatherSchema().dump(weather_schema)
    with open('weather_schema.json', 'w', encoding='UTF-8') as file:
        json.dump(city_weather, file, ensure_ascii=False, indent=4)
    with open('weather_schema.json', 'r', encoding='UTF-8') as file:
        json_data = json.load(file)
    pprint(json_data)
