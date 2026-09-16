#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# Заполнение словаря
for city_a, (x1, y1) in sites.items():
    distances[city_a] = {}
    for city_b, (x2, y2) in sites.items():
        if city_a != city_b:
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distances[city_a][city_b] = d

print(distances)