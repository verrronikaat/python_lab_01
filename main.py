#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Верхнеуровневый модуль: меню для запуска заданий лабораторной работы."""

import importlib


MODULES = {
    1: ('00_distance', 'Расстояния между городами'),
    2: ('01_circle', 'Площадь круга и точка внутри'),
    3: ('02_operations', 'Расстановка операций (1 2 3 4 5 → 25)'),
    4: ('03_favorite_movies', 'Срезы строки с фильмами'),
    5: ('04_my_family', 'Список семьи и общий рост'),
    6: ('05_zoo', 'Работа со списком животных'),
    7: ('06_songs_list', 'Сумма длительностей песен'),
    8: ('07_secret', 'Расшифровка сообщения срезами'),
    9: ('08_garden', 'Множества цветов'),
    10: ('09_shopping', 'Магазины с минимальными ценами'),
    11: ('10_store', 'Подсчёт стоимости товаров на складе'),
}


def run_task(module_name):
    module = importlib.import_module(module_name)

    if module_name == '00_distance':
        print(module.calculate_distances(module.sites))

    elif module_name == '01_circle':
        r = 42
        print('Площадь:', module.calculate_area(r))
        print('Точка (23,34) внутри:', module.is_point_inside_circle((23, 34), r))
        print('Точка (30,30) внутри:', module.is_point_inside_circle((30, 30), r))

    elif module_name == '02_operations':
        print(module.get_expression_result())

    elif module_name == '03_favorite_movies':
        for movie in module.get_movies_by_slices(module.my_favorite_movies):
            print(movie)

    elif module_name == '04_my_family':
        print('Рост отца -', module.get_father_height(module.my_family_height), 'см')
        print('Общий рост моей семьи -', module.get_total_height(module.my_family_height), 'см')

    elif module_name == '05_zoo':
        res = module.process_zoo(module.zoo_initial, module.birds)
        print(res['final_zoo'])
        print('Лев сидит в клетке', res['lion_position'])
        print('Жаворонок сидит в клетке', res['lark_position'])

    elif module_name == '06_songs_list':
        print('Три песни звучат',
              module.get_duration_from_list(module.violator_songs_list,
                                            ['Halo', 'Enjoy the Silence', 'Clean']),
              'минут')
        print('А другие три песни звучат',
              module.get_duration_from_dict(module.violator_songs_dict,
                                            ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']),
              'минут')

    elif module_name == '07_secret':
        print(module.decrypt_secret(module.secret_message))

    elif module_name == '08_garden':
        res = module.analyze_flowers(module.garden, module.meadow)
        for key, value in res.items():
            print(f'{key}: {value}')

    elif module_name == '09_shopping':
        print(module.get_cheapest_shops(module.shops))

    elif module_name == '10_store':
        for product, info in module.calculate_store_value(module.goods, module.store).items():
            print(f"{product} - {info['quantity']} шт, стоимость {info['total_cost']} руб")


def run_all():
    print('Запуск всех заданий лабораторной работы\n')
    for key in sorted(MODULES):
        module_name, title = MODULES[key]
        print(f'{key}. {title}')
        run_task(module_name)
        print()


def print_menu():
    print('\nМеню заданий:')
    for key in sorted(MODULES):
        module_name, title = MODULES[key]
        print(f'  {key} - {title}')
    print('  all - выполнить все задания')
    print('  q   - выход')


def main():
    while True:
        print_menu()
        choice = input('Выберите задание: ').strip().lower()

        if choice == 'q':
            print('Выход.')
            break

        if choice == 'all':
            run_all()
            input('\nНажмите Enter, чтобы вернуться в меню...')
            continue

        if choice.isdigit() and int(choice) in MODULES:
            key = int(choice)
            module_name, title = MODULES[key]
            print(f'\n{key}. {title}')
            run_task(module_name)
            input('\nНажмите Enter, чтобы вернуться в меню...')
        else:
            print('Неизвестная команда. Попробуйте снова.')


if __name__ == '__main__':
    main()