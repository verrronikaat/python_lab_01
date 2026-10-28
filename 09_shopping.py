#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан': [
        {'name': 'печенье', 'price': 10.99},
        {'name': 'конфеты', 'price': 34.99},
        {'name': 'карамель', 'price': 45.99},
        {'name': 'пирожное', 'price': 67.99},
    ],
    'пятерочка': [
        {'name': 'печенье', 'price': 9.99},
        {'name': 'конфеты', 'price': 32.99},
        {'name': 'карамель', 'price': 46.99},
        {'name': 'пирожное', 'price': 59.99},
    ],
    'магнит': [
        {'name': 'печенье', 'price': 11.99},
        {'name': 'конфеты', 'price': 30.99},
        {'name': 'карамель', 'price': 41.99},
        {'name': 'пирожное', 'price': 62.99},
    ],
}


def get_cheapest_shops(shops_dict):
    """
    Возвращает словарь: товар -> список из 2 магазинов с минимальными ценами.
    """
    all_offers = []
    for shop_name, products in shops_dict.items():
        for product in products:
            all_offers.append({
                'name': product['name'],
                'shop': shop_name,
                'price': product['price'],
            })

    sweets = {}
    for offer in all_offers:
        name = offer['name']
        sweets.setdefault(name, []).append({
            'shop': offer['shop'],
            'price': offer['price'],
        })

    for name in sweets:
        sweets[name].sort(key=lambda item: item['price'])
        sweets[name] = sweets[name][:2]

    return sweets


if __name__ == '__main__':
    print(get_cheapest_shops(shops))