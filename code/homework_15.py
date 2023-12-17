import json
from pprint import pprint
from typing import List, Dict, Any


class JsonAppendError(Exception):
    pass


class TxtFileHandler:
    """
    Класс для работы с TXT файлами. Чтение, запись, дописывание.
    Работает со списком строк.
    """

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def read_file(self) -> List[str]:
        """
        Метод для чтения данных из TXT файла.
        Отдает список строк
        :return: List[str]
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = file.readlines()
            return self.data

    def write_file(self, data: List[str]) -> None:
        """
        Метод для записи данных в TXT файл.
        Принимает список строк
        :param data: List[str]
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            file.writelines(data)

    def append_file(self, data: List[str]) -> None:
        """
        Метод для дописывания данных в TXT файл.
        Принимает список строк
        :param data: List[str]
        """
        with open(self.filepath, 'a', encoding='utf-8') as file:
            file.writelines(data)


class JsonFileHandler:
    """
    Класс JsonFileHandler
    read_file(filepath, as_dict=False): Метод для чтения данных из JSON файла. Флаг as_dict работает аналогично как в классе CsvFileHandler. Должен быть реализован как метод экземпляра.
    write_file(filepath, data, as_dict=False): Метод для записи данных в JSON файл. Флаг as_dict работает аналогично как в классе CsvFileHandler. Должен быть реализован как метод экземпляра.
    append_file(filepath, data): Метод для дописывания данных в JSON файл. При попытке вызова этого метода должно возникать исключение TypeError с сообщением, что данный тип файла не поддерживает операцию дописывания. Должен быть реализован как метод экземпляра.
    """

    def __init__(self, filepath: str):
        self.data = None
        self.filepath = filepath

    def append_file(self, data: Any) -> None:
        """
        Метод для дописывания данных в JSON файл.
        При попытке вызова этого метода должно возникать исключение TypeError с сообщением, что данный тип файла не поддерживает операцию дописывания.
        Должен быть реализован как метод экземпляра.
        :param data: List[str]
        """
        raise JsonAppendError('Данный тип файла не поддерживает операцию дописывания')

    def read_file(self, as_dict=False) -> List[Dict] | List[List]:
        """
        Метод для чтения данных из JSON файла.
        Флаг as_dict работает аналогично как в классе CsvFileHandler.
        Должен быть реализован как метод экземпляра.
        :return: List[Dict] | List[List]
        """
        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
            return self.data

    def write_file(self, data: List[Dict] | List[List]) -> None:
        """
        Метод для записи данных в JSON файл.
        Флаг as_dict работает аналогично как в классе CsvFileHandler.
        Должен быть реализован как метод экземпляра.
        :param data: List[Dict] | List[List]
        """
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


class CsvFileHandler:
    """
    Класс CsvFileHandler
read_file(filepath, as_dict=False): Метод для чтения данных из CSV файла. По умолчанию данные должны возвращаться в виде списка списков, но при установке флага as_dict в True, данные должны возвращаться в виде списка словарей. Должен быть реализован как метод экземпляра.
write_file(filepath, data, as_dict=False): Метод для записи данных в CSV файл. По умолчанию метод должен записывать данные в виде списка списков, но при установке флага as_dict в True, данные должны записываться в виде списка словарей. Должен быть реализован как метод экземпляра.
append_file(filepath, data, as_dict=False): Метод для дописывания данных в CSV файл. Флаг as_dict работает аналогично как в методе write_file. Должен быть реализован как метод экземпляра.
    """

    def __init__(self, filepath: str, delimiter: str = ';', encoding: str = 'windows-1251'):
        self.data = None
        self.filepath = filepath
        self.delimiter = delimiter
        self.encoding = encoding

    def read_file(self, as_dict=False) -> List[Dict] | List[List]:
        """
        Метод для чтения данных из CSV файла.
        По умолчанию данные должны возвращаться в виде списка списков, но при установке флага as_dict в True, данные должны возвращаться в виде списка словарей.
        Должен быть реализован как метод экземпляра.
        :return: List[Dict] | List[List]
        """
        with open(self.filepath, 'r', encoding=self.encoding) as file:
            self.data = file.readlines()
            if as_dict:
                return [dict(zip(self.data[0].split(self.delimiter), line.split(self.delimiter))) for line in
                        self.data[1:]]
            else:
                return [line.split(self.delimiter) for line in self.data]

    def write_file(self, data: List[Dict] | List[List], as_dict=False) -> None:
        """
        Метод для записи данных в CSV файл.
        По умолчанию метод должен записывать данные в виде списка списков, но при установке флага as_dict в True, данные должны записываться в виде списка словарей.
        Должен быть реализован как метод экземпляра.
        :param as_dict: bool
        :param data: List[Dict] | List[List]
        """
        with open(self.filepath, 'w', encoding=self.encoding) as file:
            if as_dict:
                file.writelines([self.delimiter.join(data[0].keys()) + '\n'])
                for line in data:
                    file.writelines([self.delimiter.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([self.delimiter.join(line) + '\n'])

    def append_file(self, data: List[Dict] | List[List], as_dict=False) -> None:
        """
        Метод для дописывания данных в CSV файл.
        Флаг as_dict работает аналогично как в методе write_file.
        Должен быть реализован как метод экземпляра.
        :param as_dict: bool
        :param data: List[Dict] | List[List]
        """
        with open(self.filepath, 'a', encoding=self.encoding) as file:
            if as_dict:
                for line in data:
                    file.writelines([self.delimiter.join(line.values()) + '\n'])
            else:
                for line in data:
                    file.writelines([self.delimiter.join(line) + '\n'])


list_of_students = [
    ['Фамилия', 'Имя', 'Возраст'],
    ['Иванов', 'Иван', '20'],
    ['Петров', 'Петр', '21'],
    ['Сидоров', 'Сидор', '22'],
]

csv_handler = CsvFileHandler('students.csv')

csv_handler.write_file(list_of_students)

students_list = csv_handler.read_file()
students_dict = csv_handler.read_file(as_dict=True)

pprint(students_list)
pprint(students_dict, sort_dicts=False)