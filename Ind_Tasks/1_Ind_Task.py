#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import datetime

if __name__ == '__main__':
    # Список данных о людях.
    people = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input("Введите команду >>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о человеке.
            name = input("Фамилия Имя: ")
            number = int(input("Номер телефона: "))
            bday = list(map(int, input("Дата рождения: ").split('.')))
            d_bday = datetime.date(bday[2], bday[1], bday[0])

            # Создать словарь.
            person = {
                'name': name,
                'number': number,
                'birthday': d_bday,
            }
            # Добавить словарь в список.
            people.append(person)

            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('d_bday', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 14
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^14} |'.format(
                    "№",
                    "Фамилия Имя",
                    "Номер телефона",
                    "Дата рождения"
                )
            )
            print(line)

            # Вывести данные о всех людях.
            for idx, person in enumerate(people, 1):
                print(
                    f'| {idx:>4} |'
                    f' {person.get("name", ""):<30} |'
                    f' {person.get("number", 0):<20} |'
                    f' {person.get("birthday")}      |'
                )
            print(line)

        elif command.startswith('select'):
            nomer = int(input("Введите номер телефона: "))

            # Инициализировать счетчик.
            flag = 0
            # Проверить сведения людей из списка.
            for person in people:
                if nomer == person.get('number', ''):
                    print(person.get('name', ''))
                    flag = 1
            # Если счетчик равен 0, то людей с данным номером не найдены.
            if flag == 0:
                print("Человек с данным номером не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select - запросить номер телефона человека;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.\n")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
