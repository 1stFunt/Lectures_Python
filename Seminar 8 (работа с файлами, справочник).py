# Создать телефонный справочник с возможностью импорта и экспорта данных 
# дополнить функционалом добавления информации, удаления и редактирования.

import json

db_path = 'phone book.json'
welcome = 'Enter command: 1 - read & show | 2 - search | 3 - add record | 4 - delete record | 5 - edit record | q = Quit\n'
phone_book = {}

def print_book(book):            # красивый вывод
    for k, v in phone_book.items():  
        print(k, '-', end=' | ')
        for i, j in v.items():
            print(i, j, end=' | ')
        print()

def save_db(path, db):
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(db, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
    print('БД успешно сохранена')

def load_db(path):               # загрузить из json
    fname = 'BD.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успешно загружена')
    return BD_local

def add_record(book):            # добавления информации
    key = input ('Введите новое имя: ')
    a = {}
    a['phone'] = list(input('Введите телефон: ').split())
    a['birthaday'] = input('Введите день рождения: ')
    a['email'] = input('Введите почту: ')
    book[key] = a

def edit_key(obj, old_key, new_key): # Рекурсивная функция для изменения главного ключа
    if isinstance(obj, dict):
        keys = list(obj.keys())  # Создание списка ключей словаря
        for k in keys:
            v = obj[k]
            if k == old_key:
                obj[new_key] = obj.pop(k)
            else:
                edit_key(v, old_key, new_key)

def find_values(obj, key):       # функция для поиска значения по ключу
    result = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                result.append(v)
            elif isinstance(v, (dict, list)):
                result += find_values(v, key)
    elif isinstance(obj, list):
        for item in obj:
            result += find_values(item, key)
    return result

def delete_subobjects(obj, key): # функция для удаления вложенных объектов по ключу
    if isinstance(obj, dict):
        if key in obj:
            del obj[key]
        for k, v in obj.items():
            delete_subobjects(v, key)
    elif isinstance(obj, list):
        for item in obj:
            delete_subobjects(item, key)

try:
    phone_book = load_db(db_path)
except:
    phone_book = {'Сергей риелтор': {'phone': [
        '8(918)7777777', '8(918)6666666'], 'birthday': '01.01.2000', 'email': 'serg@mail.ru'}, 'Petr': {'phone': '8(918)5555555'}}
    print('База данных не найдена. Создана тестовая база данных')

action = None
while action != 'q':
    action = input(f'{welcome}').lower()
    if action == '1':
        print_book(phone_book)
    elif action == '2':
        search_key = input('Введите имя так, как оно сохранено в справочнике: ')
        values = find_values(phone_book, search_key)
        print(search_key, "-", values)
    elif action == '3':
        add_record(phone_book)
    elif action == '4':
        search_value = input('Введите имя, которое нужно удалить из справочника: ')
        delete_subobjects(phone_book, search_value)
    elif action == '5': 
        old_key = input('Введите имя, которое нужно отредактировать: ')
        new_key = input('Введите изменения: ')
        edit_key(phone_book, old_key, new_key)
save_db(db_path, phone_book)        