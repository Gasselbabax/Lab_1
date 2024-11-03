# TODO Функция count_letters

def count_letters(text):
    text = text.lower()
    letters_duct = {}

    for letter in text:
        if letter.isalpha():
            letters_duct[letter] = letters_duct.get(letter, 0) + 1
            # TODO Метод get() позволяет взять значение, тем самым мы можем увеличивать количество букв тексте,
            # TODO если же буквы ещё нет, но она может встетиться далее, то устанавливаем значение 1
    return letters_duct

# TODO Функция calculate_frequency

def calculate_frequency(letters):
    total_letters = sum(letters.values())
    letters_frequency = {}

    for letter, frequency in letters.items():
        letters_frequency[letter] = frequency / total_letters

    return letters_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

count_text = count_letters(main_str)

new_frequency_text = calculate_frequency(count_text)

for char, percent in new_frequency_text.items():
    print(f"{char}: {percent:.2f}")
