#import telebot
from random import *
import json
#import requests
sp = {}

def save():
    with open("contacts.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(sp, ensure_ascii=False))
    print("Контакты были успешно сохранены в файле contacts.json")


def load():
    global sp
    with open("contacts.json", "r", encoding="utf-8") as fh:
        sp = json.load(fh)
    print("Контакты успешно загружены!")


try:
    load()
except:
    sp = {
        'дядя коля': {'номер телефона': ['8-800-555-35-35', '8-900-536-35-35'], 'город': 'Сыктыфкар', 'Статус': 'дядя'},
        'нюрка': {'номер телефона': ['8-555-549-34-35'], 'город': 'Сыктыфкар', 'Статус': 'тетя'}}

while True:
    command = input('Введите команду: ')
    if command == '/all':
        print('Вот текущий список номеров: ')
        for k, v in sp.items():
            print(k, v)
    elif command == '/add':
        name = input('Введите имя нового контакта: ')
        if name in sp:
            print('Контакт существует!')
        else:
            count = int(input('Сколько номеров вы хотите ввести: '))
            numbers = []
            for i in range(count):
                number = input(f'Введите {i + 1} номер: ')
                numbers.append(number)
            city = input('Введите название города: ')
            status = input('Введите статус: ')
            sp[name] = {'номер телефона': numbers, 'город': city, 'Статус': status}
            print("Контакт успешно добавлен!")
    elif command == "/save":
        save()
    elif command == "/del":
        contact = input("Введите название контакта:")
        if contact in sp:
            sp.pop(contact)
            print("Контакт успешно удалён!")
        else:
            print("Такого контакта не существует!")
    elif command == '/add.number':
        name = input('Введите имя контакта: ')
        if name not in sp:
            print('Контакта не существует!')
        else:
            phone = input('Введите номер: ')
            if phone in sp[name]['номер телефона']:
                print('Номер существует')
            else:
                sp[name]['номер телефона'].append(phone)
                print("Номер успешно добавлен!")
    elif command == "/save":
        save()
    elif command == "/stop":
        answer = input("Сохранить изменения? Если 'Да' нажмите 'y' и ENTER, если 'нет' просто нажмите ENTER: ")
        if answer == 'y':
            save()
            print("Программа завершён. Спасибо")
            break
        else:
            print("Программа завершён. Спасибо")
            break
    elif command == "/search":
        name = input("Введите имя контакта: ")
        for item in sp:
            if name not in sp:
                print('Контакта не существует!')
        else:
            print(sp[name])
    elif command == "/edit":
        name = input("Введите имя контакта: ")
        for item in sp:
            if name not in sp:
                print('Контакта не существует!')
            else:
                key = item
        new_name = input(f"Введите новое название контакта {name} - ")
        sp[new_name] = sp.pop(key)
        print("Имя контакта изменён!")
    else:
        print("Неопознанная команда. Изучите мануал через /help")

