#!/usr/bin/env python3
# -*- coding: utf-8 -*-

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99}
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99}
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99}
    ],
}

# Шаг 1: собираем все предложения в один список
all_offers = []   # [{'name': ..., 'shop': ..., 'price': ...}, ...]

for shop_name, products in shops.items():
    for product in products:
        all_offers.append({
            'name': product['name'],
            'shop': shop_name,
            'price': product['price'],
        })

# Шаг 2: группируем по названию товара
sweets = {}

for offer in all_offers:
    name = offer['name']
    if name not in sweets:
        sweets[name] = []
    sweets[name].append({
        'shop': offer['shop'],
        'price': offer['price'],
    })

# Шаг 3: сортируем по цене и оставляем 2 самых дешёвых
for name in sweets:
    sweets[name].sort(key=lambda item: item['price'])
    sweets[name] = sweets[name][:2]

print(sweets)