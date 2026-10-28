#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщлб6',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедьв9фк9ехб1а',
]


def decrypt_secret(message_list):
    """Возвращает расшифрованную фразу."""
    word1 = message_list[0][3]          # 'в'
    word2 = message_list[1][9:13]       # 'бане'
    word3 = message_list[2][5:15:2]     # 'веник'
    word4 = message_list[3][12:6:-1]    # 'дороже'
    word5 = message_list[4][20:15:-1]   # 'денег'
    return f'{word1} {word2} {word3} {word4} {word5}'


if __name__ == '__main__':
    print(decrypt_secret(secret_message))