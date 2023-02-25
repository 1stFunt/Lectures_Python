import json

# BD = [12345, True, "2023 год", {"Миша": [898981646, 464654654]}]

def load():
    # загрузить из json
    fname = 'BD.json'  # открываем файл
    with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успещно загружена')
    return BD_local

def save():
    # сохранить в json
    with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(BD, ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
    print('БД успещно сохранена')

# save()
BDnew = load()
print(BDnew)