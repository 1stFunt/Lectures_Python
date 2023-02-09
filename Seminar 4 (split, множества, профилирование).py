# # Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# # уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# text = input().split()
# text1 = {}
# for i in text:
#     if i in text1:
#         text1[i] += 1
#         print(f'{i}_{text1[i]}', end=' ')
#     else:
#         print(i, end=' ')
#         text1[i] = 0

# # Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# # подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# text = input().split()
# set_result = set()
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))
# # или в одну строку
# print(len(set(input().lower().split())))

n = int(input())
max_number = 0
while n != 0:
    if max_number < n:
        max_number = n
    n = int(input())
print(max_number)