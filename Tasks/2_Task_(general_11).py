#!/usr/bin/env python 3
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    dict_1 = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four'
    }

    new_dict = {value: key for key, value in dict_1.items()}
    print("Исходный словарь:\n", dict_1)
    print("\nОбратный словарь:\n", new_dict)
