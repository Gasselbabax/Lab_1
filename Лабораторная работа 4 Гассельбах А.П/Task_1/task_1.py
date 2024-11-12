import json  # Импортируем модуль json для работы с JSON-файлами

FILENAME = "input.json"  # Определяем имя файла, из которого будем читать данные


def task() -> float:
    """
    Функция для вычисления суммы произведений (score * weight).
    """
    # Открываем файл FILENAME для чтения
    with open(FILENAME, 'r') as input_f:
        # Загружаем данные из JSON-файла в виде списка словарей
        data = json.load(input_f)

    # Создаем список произведений score * weight, округленных до трех знаков после запятой согласно заданию
    multiple = [round(items['score'] * items['weight'], 3) for items in data]

    # Возвращаем сумму всех произведений
    return sum(multiple)


# Вызываем функцию task() и печатаем результат
print(task())
