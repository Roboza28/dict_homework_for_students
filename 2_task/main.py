"""
Вы очень любите считать. Не важно что, где и когда, главное посчитать все, что можно.
Вам на вход приходит текст. Ваша программа должна посчитать количество слов в этом тексте и вывести на печать 10
самых частых слов. Если слова встречаются одинаковое количество раз, то они должны быть отсортированы по алфавиту.

Ограничения:
- игнорируем знаки препинания (тире, запятые, многоточия и т.п.)
- слово, это все то, что отделено пробелом, символом табуляции или символом перевода строки.
- регистр игнорируется
- слова короче 3-х символов игнорируются.


Советы:
1) почитать про регулярные выражения в питоне, для визуального представления можно пользоваться сайтом https://regex101.com/
2) вспомнить про sorted, почитать про lambda функции и сортировку с их помощью

для тестирования запустить pytest 2_task/test.py
"""
from collections import Counter
import re


def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    #text_split_and_sort = sorted(re.split(r'\W+', text.lower()))
    #print(text_split_and_sort)
    correct_word = sorted(re.findall(r'\b\w{3,}\b', text.lower()))
    #correct_word = []
    small_word = 3
    #for word in text_split_and_sort:
    #    if len(word) >= small_word:
    #        correct_word.append(word)
    most_common = dict(Counter(correct_word).most_common(10))
    print()
    return most_common

