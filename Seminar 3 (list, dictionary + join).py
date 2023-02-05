# Вывести кол-во уникальных элементов.
list_1 = [1, 3, 4, 5, 5, 5, 6, 7]
result_list = list()
for i in list_1:
    if i not in result_list:
        result_list.append(i)
print(result_list)
print(len(result_list))
# или
list_1 = [1, 3, 4, 5, 5, 5, 6, 7]
result_list = list()
u = list_1.union(result_list)
print(u)
print(len(u))
# или
list_1 = [1, 3, 4, 5, 5, 5, 6, 7]
result_list = set(list_1)
print(result_list)
print(len(result_list))

# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо.
list_1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list_1)
list_result = list()
for i in range(k):
    list_result.append(list_1[len(list_1) - k + i])
for i in range(len(list_1) - k):
    list_result.append(list_1[i])
print(list_result)
# или
list_1 = [1, 2, 3, 4, 5]
k = int(input())
k = k % len(list_1)
for i in range(k):
    list_1.insert(0, list_1.pop(-1))
print(list_1)

# Напишите программу для печати всех уникальных значений в словарях.
list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {
    "VII": "S005"}, {"V ": "S009"}, {"VIII": "S007"}]
set_1 = set()
for i in list_1:
    for j in i:
        set_1.add(i[j])
print(set_1)
# или способы, как в 1ой задаче

# Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)
n = [0, -1, 5, 2, 3]
count = 0
list_1 = list()
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        count += 1
        list_1.append((n[i], n[i + 1]))
print(f"{count} ({', '.join([str(i[0]) + ' < ' + str(i[1]) for i in list_1])})")