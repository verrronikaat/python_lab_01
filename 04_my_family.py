#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья
my_family = ['мама', 'папа', 'я', 'бабушка', 'дедушка']

# список списков приблизительного роста членов вашей семьи
my_family_height = [
    ['мама', 165],
    ['папа', 180],
    ['я', 175],
    ['бабушка', 160],
    ['дедушка', 170],
]

# Рост отца
print('Рост отца -', my_family_height[1][1], 'см')

# Общий рост семьи
total_height = 0
for person in my_family_height:
    total_height += person[1]

print('Общий рост моей семьи -', total_height, 'см')