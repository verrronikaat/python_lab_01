#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def calculate_distances(sites_dict):
    """Возвращает словарь словарей расстояний между городами."""
    distances = {}
    for city_a, (x1, y1) in sites_dict.items():
        distances[city_a] = {}
        for city_b, (x2, y2) in sites_dict.items():
            if city_a != city_b:
                d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                distances[city_a][city_b] = d
    return distances


if __name__ == '__main__':
    print(calculate_distances(sites))