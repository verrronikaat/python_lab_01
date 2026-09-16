#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список животных в зоопарке
zoo = ['lion', 'kangaroo', 'elephant', 'monkey']

# Посадите медведя (bear) между львом и кенгуру
zoo.insert(1, 'bear')
print(zoo)

# Добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark']
zoo.extend(birds)
print(zoo)

# Уберите слона (elephant) из зоопарка
zoo.remove('elephant')
print(zoo)

# Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть 1-индексированными
print('Лев сидит в клетке', zoo.index('lion') + 1)
print('Жаворонок сидит в клетке', zoo.index('lark') + 1)