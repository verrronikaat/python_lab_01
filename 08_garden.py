#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# На лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')


def analyze_flowers(garden_tuple, meadow_tuple):
    """
    Возвращает словарь:
      - 'all': все виды цветов
      - 'both': растут и там, и там
      - 'only_garden': только в саду
      - 'only_meadow': только на лугу
    """
    garden_set = set(garden_tuple)
    meadow_set = set(meadow_tuple)
    return {
        'all': garden_set | meadow_set,
        'both': garden_set & meadow_set,
        'only_garden': garden_set - meadow_set,
        'only_meadow': meadow_set - garden_set,
    }


if __name__ == '__main__':
    result = analyze_flowers(garden, meadow)
    print('Все виды цветов:', result['all'])
    print('Растут и в саду, и на лугу:', result['both'])
    print('Только в саду:', result['only_garden'])
    print('Только на лугу:', result['only_meadow'])