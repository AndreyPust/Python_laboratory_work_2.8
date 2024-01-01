#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Необходимо использовать словарь, содержащий следующие ключи: название пункта
назначения, номер поезда, время отправления. Написать программу, выполняющую
следующие действия: ввод с клавиатуры данных в список, состоящий из словарей
заданной структуры; записи должны быть упорядочены по времени отправления поезда;
вывод на экран информации о поездах, направляющихся в пункт, название которого
введено с клавиатуры; если таких поездов нет, выдать на дисплей соответствующее сообщение.
Необходимо оформить команды в виде отдельных функций.
"""

import sys


def get_station(stations):
    """
    Функция запроса данных о станции.
    """
    name = input("Название пункта: ")
    # Создать словарь.
    station = {'name': name}
    print("Добавить поезд? n/y")
    cucle = input()
    if cucle == 'n':
        station['train'] = 'Поездов нет'
        station['time'] = ' '
    else:
        train = input("Номер поезда: ")
        dep_time = input("Время отправления поезда: ")
        # Добавить в словарь поезд и время.
        station['train'] = train
        station['time'] = dep_time

    # Добавить словарь в список.
    stations.append(station)

    # Отсортировать список в случае необходимости по времени поезда.
    if len(stations) > 1:
        stations.sort(key=lambda item: item.get('time', ''))

    return stations


def info(stations, name_station):
    """
    Функция вывода информации о введенной станции, о поездах и их времени (если они есть).
    Функция ничего не возвращает.
    """
    count = 0
    for station in stations:
        if station.get('name') == name_station:
            count += 1
            print("Номер поезда пункта: ", station.get('train'),
                  "Время отправления: ", station.get('time'))

    # Если счетчик равен 0, то станции не найдены.
    if count == 0:
        print("Станции не найдены.")

    return None


def help_command():
    """
    Функция вывода справочной информации о доступных командах, ничего не возвращает.
    """
    print("Список команд:\n")
    print("add - добавить станцию;")
    print("info <станция> - запросить информацию о станции;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

    return None


def main():
    """
    Главная функция программы.
    """
    # Список пунктов (станций).
    stations = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            get_station(stations)

        elif command.startswith('info '):
            # Разбить команду на части для выделения названия пункта.
            name_station = command.split(' ', maxsplit=1)
            name_station = name_station[1]
            # Вызвать функцию вывода информации о станции.
            info(stations, name_station)

        elif command == 'help':
            help_command()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
