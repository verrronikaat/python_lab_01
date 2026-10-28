#!/usr/bin/env python3
# -*- coding: utf-8 -*-

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def calculate_store_value(goods_dict, store_dict):
    result = {}
    for product_name, code in goods_dict.items():
        batches = store_dict.get(code, [])
        total_quantity = sum(batch['quantity'] for batch in batches)
        total_cost = sum(batch['quantity'] * batch['price'] for batch in batches)
        result[product_name] = {
            'quantity': total_quantity,
            'total_cost': total_cost,
        }
    return result


if __name__ == '__main__':
    for product, info in calculate_store_value(goods, store).items():
        print(f"{product} - {info['quantity']} шт, стоимость {info['total_cost']} руб")