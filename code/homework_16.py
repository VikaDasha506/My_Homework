from abc import ABC, abstractmethod


class SmartHome(ABC):
    def __init__(self, name: str):
        self.name = name  # атрибут класса

    """
    Класс Умный дом.
    Абстрактные методы:
    enable():включить
    disable():выключить
    get_state():получить_состояние
    """

    @abstractmethod
    def enable(self):
        """включить"""
        pass

    @abstractmethod
    def disable(self):
        """выключить"""
        pass

    @abstractmethod
    def get_state(self):
        """текущее состояние"""
        pass


class UrgentNotificationMixin:
    """
    Миксин для отправки срочного уведомления
    """

    def send_urgent_notification(self, notification: str):
        print(f'Срочное уведомление!: "{notification}"')


class WifiMixin:
    """Миксин для подключения к wifi"""

    def wifi(self, network_name, password):
        print(f'Имя сети: "{network_name}", Пароль: "{password}"')


class WorkScheduleMixin:
    """Миксин для создания расписания"""

    def __init__(self):
        self.schedule = {}

    def set_schedule(self, schedule):
        self.schedule = schedule
        print(f'График работы: {schedule}')


class SmartLamp(SmartHome, WifiMixin):
    def __init__(self, name):
        super().__init__(name)
        self.condition: bool = False
        self.brightness: int = 0

    def enable(self):
        self.condition: bool = True
        print(f'"{self.name}": Включен.')

    def disable(self):
        self.condition: bool = False
        print(f'"{self.name}": Выключен.')

    def get_state(self):
        if self.condition:
            return f'"{self.name}" Включена.'
        else:
            return f'"{self.name}" Выключена.'

    def brightness_adjustment(self, brightness: int):  # регулировать_яркость
        if brightness < 50:
            return f'"{self.name}": Умеренная яркость'
        else:
            return f'"{self.name}": Чрезмерная яркость. Рекомендуется убавить!'


class SmartSmokeDetector(SmartHome, UrgentNotificationMixin):
    def __init__(self, name):
        super().__init__(name)
        self.condition: bool = False

    def enable(self):
        self.condition: bool = True
        print(f'"{self.name}": Дым есть.')

    def disable(self):
        self.condition: bool = False
        print(f'{self.name}": Дыма нет')

    def get_state(self):
        if self.condition:
            return f'"{self.name}": В доме обнаружено задымление!'
        else:
            return f'"{self.name}": Дым в доме отсутствует.'


class SmartHumidifier(SmartHome, WorkScheduleMixin):
    def __init__(self, name):
        super().__init__(name)
        self.condition: bool = False
        self.air = 0

    def enable(self):
        self.condition: bool = True
        print(f'"{self.name}": Включен.')

    def disable(self):
        self.condition: bool = False
        print(f'"{self.name}": Выключен.')

    def get_state(self):
        if self.condition:
            return f'"{self.name}": Включен.'
        else:
            return f'"{self.name}": Выключен.'

    def humidity_level(self, air: int):
        if air < 10:
            return f'"{self.name}": Уровень влажности меньше необходимого!'
        else:
            return f'"{self.name}": Уровень влажности в норме.'


smart_lamp = SmartLamp('Умная лампочка')
smart_smoke_detector = SmartSmokeDetector('Умный датчик дыма')
smart_humidifier = SmartHumidifier('Умный увлажнитель воздуха')

# Управление устройствами
smart_lamp.enable()  # лампа включена
smart_lamp.disable()  # лампа выключена
smart_smoke_detector.enable()  # дым есть
smart_smoke_detector.disable()  # дыма нет
smart_humidifier.enable()  # увлажнитель включен
smart_humidifier.disable()  # увлажнитель выключен

# Вывод статуса устройств
print(smart_lamp.get_state())  # состояние лампы
print(smart_lamp.brightness_adjustment(60))  # проверка на яркость
print(smart_lamp.brightness_adjustment(40))  # проверка на яркость
print(smart_smoke_detector.get_state())  # состояние дыма
print(smart_humidifier.get_state())  # состояние увлажнителя воздуха
print(smart_humidifier.humidity_level(15))  # уровень увлажнителя воздуха
print(smart_humidifier.humidity_level(5))  # уровень увлажнителя воздуха
# Создание и настройка устройств с миксинами
smart_lamp.wifi('Домашний wifi', '123456')
smart_humidifier.set_schedule({'08:00': 'включить', '23:00': 'выключить'})
# Симуляция срочного уведомления от датчика дыма
if smart_smoke_detector.get_state():
    smart_smoke_detector.send_urgent_notification('Обнаружен дым на кухне!')
