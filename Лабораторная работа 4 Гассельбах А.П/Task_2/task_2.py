import json # Импортируем модуль json для работы с JSON-файлами
import csv # Импортируем модуль csv для работы с CSV-файлами


# Названия входного и выходного файлов
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    """
    Функция для конвертации csv в json
    """

    # Открываем CSV файл для чтения
    with open(INPUT_FILENAME, 'r') as input_c:

        # Создаем DictReader для автоматической обработки строк CSV файла.
        # Каждая строка будет представлена в виде словаря, где ключи - заголовки столбцов
        need_to_read = csv.DictReader(input_c)

        # Преобразуем считанные строки в список словарей
        values = [row for row in need_to_read]

    # Открываем JSON файл для записи
    with open(OUTPUT_FILENAME, 'w') as output_j:
        # Сериализуем список словарей в JSON формат с отступами 4
        json.dump(values, output_j, indent=4)

if __name__ == '__main__':
    # Выполняем основную функцию задачи
    task()

    # Открываем JSON файл для проверки и выводим содержимое
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")