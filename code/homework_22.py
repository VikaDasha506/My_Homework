class PalindromeStrategy:
    def is_palindrome(self, string) -> bool:
        """Принимает строку, и если это палиндром, возвращает True"""
        return True


class SingleWordPalindrome(PalindromeStrategy):
    """Для проверки одиночных слов"""

    def is_palindrome(self, string):
        string = string.lower()
        if string.upper() == (string.upper()[::-1]):
            return f'Обнаружен палиндром: "{string}"'
        else:
            return f'Слово "{string} "не является палидромом!'


class MultiWordPalindrome(PalindromeStrategy):
    """Для проверки многословных выражений"""

    def is_palindrome(self, string):
        string = ''.join(i for i in string if i.isalnum()).lower()  # убираем все символы,приводим к нижнему регистру
        if string == string[::-1]:
            return f'Обнаружен палиндром: "{string}"'
        else:
            return f'"{string}" не является палидромом!'


class PalindromeContext:
    """использует PalindromeStrategy"""

    def __init__(self):
        self.strategy = PalindromeStrategy()

    def set_strategy(self, strategy):
        """Установливаем текущую стратегию"""
        self.strategy = strategy

    def check(self, string):
        """Выполняет проверку через выбранную стратегию"""
        if self.strategy:
            return self.strategy.is_palindrome(string)
        else:
            raise ValueError("Стратегия не определена")


class PalindromeFacade:
    """реализуйет логику определения, какую стратегию использовать (одиночное
       слово или многословное выражение)"""

    def __init__(self):
        """вызов методов PalindromeContext"""
        self.context = PalindromeContext()

    def determine_strategy(self, string):
        # определение, какую стратегию использовать
        if ' ' not in string:
            self.context.set_strategy(SingleWordPalindrome())
        else:
            self.context.set_strategy(MultiWordPalindrome())

    def check_palindrome(self, string):
        self.determine_strategy(string)
        return self.context.check(string)


def main():
    user_input = input("Введите одно или несколько слов: ")
    facade = PalindromeFacade()
    result = facade.check_palindrome(user_input)
    print(result)


if __name__ == "__main__":
    main()

"""А лес у села; А роза упала на лапу Азора;Буду жив, увижу дуб;
Шалаш, мадам,наган,казак"""
