#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# моя семья
my_family = ['мама', 'папа', 'я', 'бабушка', 'дедушка']

# список списков приблизительного роста членов семьи
my_family_height = [
    ['мама', 165],
    ['папа', 180],
    ['я', 175],
    ['бабушка', 160],
    ['дедушка', 170],
]


def get_father_height(family_height):
    """Возвращает рост отца (папы) из списка."""
    for name, height in family_height:
        if name == 'папа':
            return height
    return None


def get_total_height(family_height):
    """Возвращает суммарный рост всех членов семьи."""
    return sum(height for _, height in family_height)


if __name__ == '__main__':
    print('Рост отца -', get_father_height(my_family_height), 'см')
    print('Общий рост моей семьи -', get_total_height(my_family_height), 'см')