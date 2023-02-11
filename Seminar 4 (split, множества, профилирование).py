# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
text = input().split()
text1 = {}
for i in text:
    if i in text1:
        text1[i] += 1
        print(f'{i}_{text1[i]}', end=' ')
    else:
        print(i, end=' ')
        text1[i] = 0

# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
text = input().split()
set_result = set()
for i in text:
    set_result.add(i.lower())
print(len(set_result))
# или в одну строку
print(len(set(input().lower().split())))

n = int(input())
max_number = 0
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)

# Даны два неупорядоченных набора целых чисел (может быть, сповторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
list_1 = [int(x) for x in input().split()]
list_2 = [int(x) for x in input().split()]
print(list_1)
print(list_2)
list_1 = set(list_1)
list_2 = set(list_2)
print(*sorted(list_1.intersection(list_2)))