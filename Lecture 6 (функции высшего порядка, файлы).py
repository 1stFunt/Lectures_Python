#  Функция в функции, lambda - функция
def calk1(a, b):    # или сократить calk1 = lambda a, b: a + b
    return a + b
def calk2(a, b):    # ... calk2 = lambda a, b: a * b
    return a * b
def math(op, x, y):
    print(op(x, y))
math(calk2, 5, 45)  # или math(lambda a, b: a + b, 5, 45) - вместо написания функции calk1 и тд.

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
list_result = list()
for i in list_1:
    if i % 2 == 0:
        list_result.append((i, i**2))
print(list_result)
# и решение через lambda
def select(f, col):            # по сути это расписанная встроенная функция map
    return [f(x) for x in col]
def where(f, col):             # по сути это расписанная встроенная функция filter (ниже компактный пример применения - 42 строка)
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)  # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print(res)

# Функция map (применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами)
list_1 = [x for x in range(1, 20)]
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

# C клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
# Этот набор чисел будет считан в качестве строки.
data = list(map(int, input().split()))
print(data)

# Функция filter (применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True)
data = '1 2 3 5 8 15 23 38'.split()
print(data)
res = map(int, data)    # преобразовали строку к числам int
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)

# Функция zip (применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных)
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
# Функция zip () пробегает по минимальному входящему набору:
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

# Функция enumerate (применяется к итерируемому объекту и возвращает новый итератор с кортежами из индекса и элементов входных данных)
users = ['user1', 'user2', 'user3']
data = list(enumerate(users))
print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# Работа с файлами
# Режим a (открытие для добавления данных)
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')    # здесь указываем режим, в котором будем работать
data.writelines(colors)         # разделителей не будет
data.close()                    # создастся файл text со строкой redgreenblue

# ● data.close() — используется для закрытия файла, чтобы разорвать подключение файловой переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление в существующий файл, а не перезапись файлов.

# Режим w (в случае перезаписи новые данные записываются, а старые удаляются)
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')

# Режим r (чтение данных из файла)
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
    data.close()