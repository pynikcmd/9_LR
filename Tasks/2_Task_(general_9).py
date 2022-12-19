#!/bin/usr/env python3
# -/*- coding:utf-8 -*-

if __name__ == '__main__':
    school = {
        '1а': 28,
        '1б': 32,
        '4г': 25,
        '9е': 25,
        '10б': 29,
        '8в': 21
    }
    print('Первоначальный состав:\n', school)
    # Задание (a). Изменение количества учащихся.
    school['1б'] = 25

    # Задание (b). В школе новый класс.
    school['11г'] = 30

    # Задание (с). В школе был расформирован (удален) другой класс.
    # Вычислите общее количество учащихся в школе.
    del school['1б']
    s = sum(klass for klass in school.values())
    print('\nСостав после изменений:\n', school)
    print('\nОбщее количество учащихся в школе = ', s)