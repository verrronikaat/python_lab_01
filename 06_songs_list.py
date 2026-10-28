#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Песни из списка (список списков: [название, длительность])
violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Песни из словаря (название: длительность)
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


def get_duration_from_list(songs_list, wanted):
    """Суммарное время песен из списка, округлённое до 3 знаков."""
    total = sum(duration for name, duration in songs_list if name in wanted)
    return round(total, 3)


def get_duration_from_dict(songs_dict, wanted):
    """Суммарное время песен из словаря, округлённое до 3 знаков."""
    total = sum(songs_dict[name] for name in wanted)
    return round(total, 3)


if __name__ == '__main__':
    wanted_list = ['Halo', 'Enjoy the Silence', 'Clean']
    print('Три песни звучат', get_duration_from_list(violator_songs_list, wanted_list), 'минут')

    wanted_dict = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    print('А другие три песни звучат', get_duration_from_dict(violator_songs_dict, wanted_dict), 'минут')