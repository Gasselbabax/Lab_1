# TODO Функция для поиска индекса товара

def search_index(items, required_item):

    if required_item in items:
        return items.index(required_item) # TODO Если товар найден, возвращаем индекс его первого вхождения с помощью списочного метода index
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_index(items_list, find_item)  # TODO Вызвали функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
