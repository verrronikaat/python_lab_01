#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Тесты для всех заданий лабораторной работы."""

import importlib


# Динамический импорт модулей с цифровыми именами
mod_00 = importlib.import_module('00_distance')
mod_01 = importlib.import_module('01_circle')
mod_02 = importlib.import_module('02_operations')
mod_03 = importlib.import_module('03_favorite_movies')
mod_04 = importlib.import_module('04_my_family')
mod_05 = importlib.import_module('05_zoo')
mod_06 = importlib.import_module('06_songs_list')
mod_07 = importlib.import_module('07_secret')
mod_08 = importlib.import_module('08_garden')
mod_09 = importlib.import_module('09_shopping')
mod_10 = importlib.import_module('10_store')


def test_distance_structure():
    res = mod_00.calculate_distances(mod_00.sites)
    assert set(res.keys()) == {'Moscow', 'London', 'Paris'}
    assert 'London' in res['Moscow']
    assert 'Paris' in res['London']


def test_distance_values():
    res = mod_00.calculate_distances(mod_00.sites)
    assert round(res['Moscow']['London'], 2) == 145.60
    assert round(res['Moscow']['Paris'], 2) == 130.38


def test_circle_area():
    assert mod_01.calculate_area(42) == 5541.7693


def test_point_inside_1():
    assert mod_01.is_point_inside_circle((23, 34), 42) is True


def test_point_inside_2():
    assert mod_01.is_point_inside_circle((30, 30), 42) is False


def test_operations():
    assert mod_02.get_expression_result() == 25


def test_movies_slices():
    first, last, second, second_from_end = mod_03.get_movies_by_slices(
        mod_03.my_favorite_movies
    )
    assert first == 'Терминатор'
    assert last == 'Назад в будущее'
    assert second == 'Пятый элемент'
    assert second_from_end == 'Чужие'


def test_father_height():
    assert mod_04.get_father_height(mod_04.my_family_height) == 180


def test_total_height():
    assert mod_04.get_total_height(mod_04.my_family_height) == 850


def test_zoo_final_list():
    res = mod_05.process_zoo(mod_05.zoo_initial, mod_05.birds)
    assert res['final_zoo'] == [
        'lion', 'bear', 'kangaroo', 'monkey', 'rooster', 'ostrich', 'lark'
    ]


def test_zoo_positions():
    res = mod_05.process_zoo(mod_05.zoo_initial, mod_05.birds)
    assert res['lion_position'] == 1
    assert res['lark_position'] == 7


def test_zoo_original_not_modified():
    _ = mod_05.process_zoo(mod_05.zoo_initial, mod_05.birds)
    assert mod_05.zoo_initial == ['lion', 'kangaroo', 'elephant', 'monkey']


def test_songs_list_duration():
    total = mod_06.get_duration_from_list(
        mod_06.violator_songs_list, ['Halo', 'Enjoy the Silence', 'Clean']
    )
    assert total == 14.93


def test_songs_dict_duration():
    total = mod_06.get_duration_from_dict(
        mod_06.violator_songs_dict,
        ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    )
    assert total == 13.49


def test_secret_message():
    assert mod_07.decrypt_secret(mod_07.secret_message) == 'в бане веник дороже денег'


def test_garden_intersection():
    res = mod_08.analyze_flowers(mod_08.garden, mod_08.meadow)
    assert res['both'] == {'ромашка', 'одуванчик'}


def test_garden_only_garden():
    res = mod_08.analyze_flowers(mod_08.garden, mod_08.meadow)
    assert res['only_garden'] == {'гладиолус', 'роза', 'подсолнух'}


def test_garden_only_meadow():
    res = mod_08.analyze_flowers(mod_08.garden, mod_08.meadow)
    assert res['only_meadow'] == {'мак', 'клевер'}


def test_shopping_cheapest():
    res = mod_09.get_cheapest_shops(mod_09.shops)
    for product, offers in res.items():
        assert len(offers) == 2
    assert res['печенье'][0]['shop'] == 'пятерочка'
    assert res['печенье'][0]['price'] == 9.99
    assert res['печенье'][1]['shop'] == 'ашан'
    assert res['печенье'][1]['price'] == 10.99
    assert res['конфеты'][0]['shop'] == 'магнит'
    assert res['конфеты'][0]['price'] == 30.99


def test_store_totals():
    res = mod_10.calculate_store_value(mod_10.goods, mod_10.store)
    assert res['Лампа'] == {'quantity': 27, 'total_cost': 1134}
    assert res['Стол'] == {'quantity': 54, 'total_cost': 27860}
    assert res['Диван'] == {'quantity': 3, 'total_cost': 3550}
    assert res['Стул'] == {'quantity': 105, 'total_cost': 10311}