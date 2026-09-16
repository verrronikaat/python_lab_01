#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

# Три песни из списка
wanted_list = ['Halo', 'Enjoy the Silence', 'Clean']
total_list = 0
for song in violator_songs_list:
    if song[0] in wanted_list:
        total_list += song[1]

print('Три песни звучат', round(total_list, 3), 'минут')


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

# Три другие песни из словаря
wanted_dict = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
total_dict = 0
for name in wanted_dict:
    total_dict += violator_songs_dict[name]

print('А другие три песни звучат', round(total_dict, 3), 'минут')