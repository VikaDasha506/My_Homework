import csv
from typing import (List, Dict, Tuple, Set, Union,
                    Optional, Any, Callable, Iterable, Iterator, Generator)


# №1
def password_checker(func: Callable) -> Callable:
    def wrapper(password):
        try:
            if len(password) < 8:
                raise TypeError(f'Пароль "{password}" должен содержать не менее 8 символов')
            if password.isupper() or password.islower():
                raise TypeError(f'В пароле "{password}" должны содержаться буквы разного регистра!')
            if password.isalnum():
                raise TypeError(f'Пароль "{password}" должен содержать спецсимволы!')
            if not any(symbol.isdigit() for symbol in password):
                raise TypeError(f'Пароль "{password}" должен содержать хотя бы одну цифру!')
            func(password)
        except TypeError as e:
            print(f"Ошибка: {e}")

    return wrapper


@password_checker
def register_user(password_user):
    if password_user:
        print('Регистрация прошла успешно!')


register_user('Qwerty123.')
register_user('QWERTy123.')
register_user('QWERTY123.')
register_user('Qwerty123')
register_user('Qwerty')
register_user('Qwertyqw.')
register_user('qwer123.')


# №2
def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1) -> Any:
    """
    Функция проверяет сложность пароля согласно условиям:
    :param length: минимальная длина пароля (по умолчанию = 8)
    :param uppercase: минимальное количество заглавных букв (по умолчанию = 1)
    :param lowercase: минимальное количество строчных букв (по умолчанию = 1)
    :param special_chars: минимальное количество спецсимволов (по умолчанию = 1)
    :return:
    """

    def validator(func: Callable) -> Callable:
        """
        :param func: функция, которую принимает декоратор на проверку пароля
        :return:
        """

        def wrapper(password: str, user: str) -> None:
            """
            Функция проверяет пароль на сложность
            :param password: пароль, вводимый пользователем
            :param user: имя, введенное пользователем
            :return: None
            """
            try:
                if len(password) < length:
                    raise ValueError(f'Пароль должен содержать не менее {length} символов')
                letter_upper: int = sum(letter.isupper() for letter in password)
                if letter_upper < uppercase:
                    raise ValueError(f'Пароль должен содержать минимум {uppercase} буквы верхнего регистра!')
                letter_lower: int = sum(letter.isupper() for letter in password)
                if letter_lower < lowercase:
                    raise ValueError(f'Пароль должен содержать минимум {lowercase} буквы нижнего регистра!')
                chars: int = sum(1 for char in password if not char.isalnum())
                if chars < special_chars:
                    raise ValueError(f'Пароль должен содержать минимум {special_chars} спецсимвол!')
                func(password, user)
            except ValueError as e:
                print(f'Ошибка: {e}')

        return wrapper

    return validator


def username_validator(func: Callable) -> Callable:
    """
    Функция проверяет, что в имени пользователя отсутствуют пробелы.
    :param func: функция, которую принимает декоратор на проверку имени пользователя
    :return:None
    """

    def wrapper(password: str, user: str) -> None:
        try:
            if ' ' in user:
                raise ValueError(f'В имени пользователя есть пробелы!')
            func(password, user)
        except ValueError as e:
            print(f'Ошибка: {e}')

    return wrapper


@password_validator(10, 2, 2, 2)
@username_validator
def register_user(password: str, username: str):
    """
    Функция для регистрации нового пользователя.
    :param password: принимает пароль пользователя
    :param username: принимает имя пользователя
    """
    csv_file = 'register_user_password.csv'
    with open(csv_file, 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([password, username])
    pass


# Тестирование успешного случая
try:
    register_user('!PassworD123!', 'JohnDoe', )
    print(f'Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')
# Тестирование неудачного случая по паролю
try:
    if register_user('Password123!', 'JohnDoe', ):
        print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')
# Тестирование неудачного случая по юзернейму
try:
    if register_user('!PassworD123!', 'John Doe', ):
        print('Регистрация прошла успешно!')
except ValueError as e:
    print(f'Ошибка: {e}')
