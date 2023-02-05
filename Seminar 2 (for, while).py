# for i in range(5):
#     print(i, end=' ')

# i = 0
# while i < 5:
#     i += 1
#     if i == 5:
#         print(i)
#     else:
#         print(i, end=', ')

# n = int(input('Введите число: '))
# result = 1
# i = 2
# while i <= n:
#     result *= i
#     i += 1
# print(f"Факториал числа {n} -> {result}")

# n = int(input('Введите число: '))
# a0 = 0
# a1 = 1
# count = 1
# while a0 < n:
#     x = a0 + a1
#     a0 = a1
#     a1 = x
#     count += 1
# if a0 != n:
#     print(f'Число {n} не является числом Фибоначчи')
# else:
#     print(count)

# n = int(input('Введите кол-во дней: '))
# count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input())
#     if temp > 0:
#         count += 1
#     else:
#         if max_count < count:
#             max_count = count
#         count = 0
# print(max_count)

n = int(input('Введите кол-во арбузов: '))
max = 0
min = 1000
for i in range(n):
    mass = int(input())
    if mass > max:
        max = mass
    if mass < min:
        min = mass
print(min, max)
