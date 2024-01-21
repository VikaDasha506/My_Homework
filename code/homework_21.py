from abc import ABC, abstractmethod


class IngredientFactory(ABC):
    """Абстрактный класс для фабрики ингредиентов"""

    @abstractmethod
    def create_cheese(self) -> str:
        """ Абстрактный метод, должен быть переопределен для возврата типа сыра"""
        return 'Тип сыра'

    @abstractmethod
    def create_sauce(self) -> str:
        """ Абстрактный метод, должен быть переопределен для возврата типа соуса."""
        return 'Тип соуса'


class DodoIngredientFactory(IngredientFactory):
    """Конкретная фабрика ингредиентов для Додо Пиццы"""

    def create_cheese(self) -> str:
        """ Возвращает тип сыра, используемый Додо Пиццей."""
        return 'Моцареллa'

    def create_sauce(self) -> str:
        """ Возвращает тип соуса, используемый Додо Пиццей."""
        return 'Томатный'


class SizeFactory:
    """ Управляет созданием размеров пиццы"""

    def create_size(self, size: str) -> str:
        """ Принимает название размера и возвращает его описание"""
        if size == 'Маленькая':
            return 'диаметром: 30 см'
        elif size == 'Средняя':
            return 'диаметром: 40 см'
        elif size == 'Большая':
            return 'диаметром: 50 см'
        else:
            return 'Не задан размер'


class PizzaBuilder:
    """Собирает пиццу, используя ингредиенты и размеры"""

    def __init__(self, pizza_type):
        self.ingredient_factory = DodoIngredientFactory()  # используется для получения ингредиентов
        self.size_factory = SizeFactory()  # используется для определения размера пиццы
        self.pizza_type = pizza_type  # Тип пиццы
        self.size = None  # Размер пиццы

    def set_size(self):
        """ Устанавливает размер пиццы"""
        input_size = input('Выберете размер пиццы:("Маленькая", "Средняя", "Большая"):')
        self.size = self.size_factory.create_size(input_size)

    def build(self):
        """ Собирает и возвращает описание пиццы"""
        cheese = self.ingredient_factory.create_cheese()
        sauce = self.ingredient_factory.create_sauce()
        return f'Вы выбрали пиццу: "{self.pizza_type}", {self.size}, c сыром "{cheese}" и соусом "{sauce}".'


def create_pizza():
    """ Создаёт заказ пиццы с её описанием"""
    builder = PizzaBuilder("Pepperoni")
    builder.set_size()  # запрос размера пиццы
    pizza = builder.build()  # возврат описания пиццы
    return pizza


def main():
    pizza = create_pizza()
    print(pizza)


if __name__ == "__main__":
    main()
