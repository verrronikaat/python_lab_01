#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Пи возьмём равным 3.1415926
PI = 3.1415926


def calculate_area(r):
    """Возвращает площадь круга, округлённую до 4 знаков после запятой."""
    return round(PI * r ** 2, 4)


def is_point_inside_circle(point, r):
    """True, если точка внутри круга с центром (0, 0) и данным радиусом."""
    x, y = point
    distance = (x ** 2 + y ** 2) ** 0.5
    return distance <= r


if __name__ == '__main__':
    point_1 = (23, 34)
    point_2 = (30, 30)

    print(calculate_area(radius))
    print(is_point_inside_circle(point_1, radius))
    print(is_point_inside_circle(point_2, radius))