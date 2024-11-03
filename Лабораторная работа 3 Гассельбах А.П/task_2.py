# TODO функция find_common_participants

def find_common_participants(first, second, divider = ','):
    common_members = list(set(first.split(divider)).intersection(second.split(divider)))
    #TODO используем метод множества intersection() для нахождения общих участников
    # далее преобразовываем множество в список для последующей сортировки

    common_members.sort()
    return common_members

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Проверка работы функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
