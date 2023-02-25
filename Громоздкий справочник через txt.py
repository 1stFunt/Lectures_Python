# https://gbcdn.mrgcdn.ru/uploads/record/241504/attachment/7434bed467dac4c4270b6cb7ec45b23b.mp4 - ссылка на семинар
from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass

def read_records():
    """Считывание данных из базы"""

    global all_data, last_id

    with open(file_base, "r", encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1][0])

        return all_data

def show_all():
    """Отображение содержимого базы данных"""

    if not all_data:
        print("Empty data")
    else:
        print(*all_data, sep="\n")

def add_new_contact():
    """Добавление новой записи"""

    global last_id

    array = ['surname', 'name', 'patronymic', 'phone number']
    answers = []
    for i in array:
        answers.append(data_collection(i))

    if not exist_contact(0, " ".join(answers)):
        last_id += 1
        answers.insert(0, str(last_id))

        with open(file_base, 'a', encoding="utf-8") as f:
            f.write(f'{" ".join(answers)}\n')
        print("The entry has been successfully added to the phone book!\n")
    else:
        print("The data already exists!")

def del_contact():
    """Удаление записи"""

    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Enter the record id: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Record deleted!\n")
    else:
        print("The data is not correct!")

def change_contact(data_tuple):
    """Изменение существующей записи"""

    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("The data already exists!")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Record changed!\n")

def search_contact():
    search_data = exist_contact(0, input("Enter the search data: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("The data is not correct!")

def exist_contact(rec_id, data):
    """Проверка записи в базе

    :type data: проверка записи
    :type rec_id: проверка id
    """

    if rec_id:
        candidates = [i for i in all_data if rec_id in i[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def data_collection(num):
    """Проверка полученных данных"""

    answer = input(f"Enter a {num}: ")
    while True:
        if num in "surname name patronymic":
            if answer.isalpha():
                break
        if num == "phone number":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Data is incorrect!\n"
                       f"Use only use only the letters"
                       f" of the alphabet, the length"
                       f" of the number is 11 digits\n"
                       f"Enter a {num}: ")
    return answer

def main_menu():
    """Основное меню"""

    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                exp_imp_menu()
            case "7":
                play = False
            case _:
                print("Try again!\n")

def edit_menu():
    """Меню редактирования"""

    add_dict = {"1": "surname", "2": "name", "3": "patronymic", "4": "phone number"}

    show_all()
    record_id = input("Enter the record id: ")

    if exist_contact(record_id, ""):
        while True:
            print("\nChanging:")
            change = input("1. surname\n"
                           "2. name\n"
                           "3. patronymic\n"
                           "4. phone number\n"
                           "5. exit\n")

            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("The data is not recognized, repeat the input.")
    else:
        print("The data is not correct!")

def exp_bd(name):
    """Сохранение данных в новый файл"""

    symbol = "\n"

    if not path.exists(name):
        with open(f"{name}.txt", "w", encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')

def ipm_bd(name):
    global file_base
    if path.exists(name):
        file_base = name
        read_records()

def exp_imp_menu():
    """Меню экспорта/импорта'"""

    while True:
        print("\nExp/Imp menu:")
        move = input("1. Import\n"
                     "2. Export\n"
                     "3. exit\n")

        match move:
            case "1":
                ipm_bd(input("Enter the name of the file: "))
            case "2":
                exp_bd(input("Enter the name of the file: "))
            case "3":
                return 0
            case _:
                print("The data is not recognized, repeat the input.")
main_menu()