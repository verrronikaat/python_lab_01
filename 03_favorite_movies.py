#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'


def get_movies_by_slices(movies_string):
    """Возвращает кортеж: (первый, последний, второй, второй с конца)."""
    first = movies_string[:10]
    last = movies_string[42:]
    second = movies_string[12:25]
    second_from_end = movies_string[35:40]
    return first, last, second, second_from_end


if __name__ == '__main__':
    for movie in get_movies_by_slices(my_favorite_movies):
        print(movie)