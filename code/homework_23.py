import pytest
import requests


cities = [
    ('Москва', {'lon': 37.6156, 'lat': 55.7522}),
    ('Воронеж', {'lon': 39.17, 'lat': 51.6664}),
    ('Санкт-Петербург', {'lon': 30.2642, 'lat': 59.8944}),
    ('Краснодар', {'lon': 38.9769, 'lat': 45.0328}),
    ('Сочи', {'lon': 39.7303, 'lat': 43.6}),
]


class WeatherRequest:
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


@pytest.fixture(scope="module")
def weather_request():
    weather_request = WeatherRequest('Москва').get_weather()
    return weather_request


# Тест 1
def test_weather_request_city_name(weather_request):
    response = weather_request
    assert response['name'] == 'Москва', 'Город не совпадает'


# Тест 2
@pytest.mark.parametrize('city, coord', cities)
def test_weather_request_coord(city, coord, weather_request):
    cities_coord = [city[1] for city in cities]
    assert cities_coord[0] == weather_request['coord'], "Координаты не совпадает"


# Тест 3
def test_weather_request_weather_key(weather_request):
    assert 'id' in weather_request['weather'][0], "В city['weather'][0] нет ключа id"
    assert 'main' in weather_request['weather'][0], "В city['weather'][0] нет ключа main"
    assert 'description' in weather_request['weather'][0], "В city['weather'][0] нет ключа description"
    assert 'icon' in weather_request['weather'][0], "В city['weather'][0] нет ключа icon"


# Тест 4
def test_weather_request_main_key(weather_request):
    assert 'temp' in weather_request['main'], "В weather_request['main'] нет ключа temp"
    assert 'feels_like' in weather_request['main'], "В weather_request['main'] нет ключа feels_like"
    assert 'temp_min' in weather_request['main'], "В weather_request['main'] нет ключа temp_min"
    assert 'temp_max' in weather_request['main'], "В weather_request['main'] нет ключа temp_max"
    assert 'pressure' in weather_request['main'], "В weather_request['main'] нет ключа pressure"
    assert 'humidity' in weather_request['main'], "В weather_request['main'] нет ключа humidity"


