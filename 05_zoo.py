#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo_initial = ['lion', 'kangaroo', 'elephant', 'monkey']

# Птицы, которых нужно добавить в последние клетки
birds = ['rooster', 'ostrich', 'lark']


def process_zoo(zoo, birds_list):
    """
    Выполняет операции над списком животных и возвращает словарь:
      - 'final_zoo': итоговый список
      - 'lion_position': номер клетки льва (с 1)
      - 'lark_position': номер клетки жаворонка (с 1)
    """
    zoo = zoo.copy()

    # 1) Посадить медведя между львом и кенгуру
    zoo.insert(1, 'bear')

    # 2) Добавить птиц в последние клетки
    zoo.extend(birds_list)

    # 3) Убрать слона
    zoo.remove('elephant')

    return {
        'final_zoo': zoo,
        'lion_position': zoo.index('lion') + 1,
        'lark_position': zoo.index('lark') + 1,
    }


if __name__ == '__main__':
    result = process_zoo(zoo_initial, birds)
    print(result['final_zoo'])
    print('Лев сидит в клетке', result['lion_position'])
    print('Жаворонок сидит в клетке', result['lark_position'])