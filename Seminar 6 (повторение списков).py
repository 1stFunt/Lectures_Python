# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
from random import randint
numbers = list([randint(1, 100) for i in range(int(input('Введите длину массива: ')))])
print(numbers)
count = 0
for i in range(1, len(numbers) - 1):
    if numbers[i - 1] < numbers[i] > numbers [i + 1]:
        count += 1
print(count)

# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
list_1 = [int(i) for i in input().split()]      # или list_1 = list(map(int, input().split()))
counter = 0
print(list_1)
for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if list_1[i] == list_1[j]:
            counter += 1
print(counter)
# или
from collections import Counter
numbers = [1, 2, 3, 2, 3]
dictionary = Counter(numbers)
for key, values in dictionary.items():
    if int(values)//2:
        print(f'{key}, колличество пар {int(values)//2}')