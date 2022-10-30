main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
my_dict = {}
for letter in main_str.lower():
    if letter.isalpha():
        my_dict[letter] = 0


def get_count_char(str_):
    count_dict = my_dict
    for letter in str_.lower():
        if letter.isalpha():
            count_dict[letter] += 1
    return count_dict


def get_perc_char(count_dict):
    perc_dict = count_dict
    for letter in perc_dict:
        perc_dict[letter] = perc_dict[letter] / sum(perc_dict.values()) * 100
    return perc_dict


count_dict = get_count_char(main_str)
print(count_dict)
# print(get_perc_char(count_dict))
# комментирую строку для того, чтобы вывод совпал
