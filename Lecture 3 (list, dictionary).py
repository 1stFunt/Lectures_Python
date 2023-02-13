# append - функция добавляет новое значение в конец списка, len - кол-во элементов в объекте.
list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)
print(len(list_1))

list_1 = []
for i in range(5):
    list_1.append(i)
    print(list_1)

# Удаление последнего элемента списка (pop())
list_1 = [1, 4, 134, 56, -23]
print(list_1.pop())
print(list_1)

# Удаление конкретного элемента из списка (pop(индекс))
list_1 = [1, 4, 134, 56, -23]
print(list_1.pop(-2))
print(list_1)

# Добавление элемента на нужную позицию (insert (индекс позиции, элемент))
list_1 = [1, 4, 134, 56, -23]
print(list_1.insert(2, 11))
print(list_1)

list_1 = [1, 4, 134, 56, -23, 5, 8, 9]
print(list_1[::6])   # сначала до конца с шагом 6 [1, 8]

# Кортеж, класс 'tuple' - неизменяемые списки, быстрее.
t = (1,)                # для создания кортежа после числа писать запятую
print(*t)

# Преобразование списка в кортеж
v = [1, 4, 4]
v = tuple(v)
print(type(v))
print(v)
a, b, c = v   # Раскрытие списка
print(a, b, c)

t = (1, 4, 5, 3, 5,) # вывод списка
for i in t:
    print(i, end=' ')
# или
t = (1, 4, 5, 3, 5,)
for i in range(len(t)):
    print(t[i], end=' ')

# Словари 'dictionary' с доступом по ключу.
d = {}  # или d = dict()
d['q'] = 'qwerty' # q - ключ. Добавляем значение в словарь.
print(d)
# Либо если нужно добавить несколько значений
d.update({'four': 4, 'five': 5})
print(d) 

dictionary = {}
dictionary = {'right': '->', 'left': '<-'}
print(dictionary['right'])      # Или через get - print(dictionary.get('right')). Через get можно выводить элемент,  
dictionary[895] = 123           # заданный по умолчанию через второй аргумент.
print(dictionary)

dictionary = {'right': '->', 'left': '<-'}
del dictionary['left']   # удаление элемента. Или dictionary.pop('left')
for item in dictionary:
    print(item)          # вывод ключей. Или print(dictionary.keys())
print('{}:{}'.format(item, dictionary[item])) # вывод ключ + элемент
# или
for (k, v) in dictionary.items():
    print(k, v)
# Вывод только значений
print(dictionary.values())

# Вложенный словарь
dict1 = {'Tom': {'English': 5, 'Math': 5}, 'Red': {'English': 4, 'Math': 4}}
# print(dict1['Tom'])
for i in dict1['Tom'].items(): # вывод в список по строкам
    print(*i)
# или
print(dict1['Red']['Math'])
# Добавление элементов во вложенный словарь
dict1.update({'Wer': {'English': 3, 'Math': 3}})
# и
dict1['Tom'].update({'Trud': 5})
print(dict1)

# Множества - уникальные элементы, не повторяются и не индексируются!
colors = {'red', 'green', 'black'} # или q = set()
print(colors)

# Операции со множествами!!!
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()             # с = {1, 2, 3, 5, 8}
u = a.union(b)           # u = {1, 2, 3, 5, 8, 13, 21} - объединение уникальных значений
i = a.intersection(b)    # i = {8, 2, 5} - пересечение в обеих множествах
d1 = a.difference(b)     # d1 = {1, 3} - разница между a и b
d2 = b.difference(a)     # d2 = {13, 21} - разница между b и a
q = a.union(b).difference(a.intersection(b)) # q = {1, 21, 3, 13} - сначало правая часть, потом левая и потом разница
print(q)

# Заморозка множества
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)

# Генерация списков без использования перебирания (for)
list_1 = [i for i in range (1, 100)]
print(list_1)

list_1 = [i for i in range(1, 100) if i % 2 == 0]  # только чётные числа в список
print(list_1)

list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)