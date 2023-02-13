# Рекурсия Фибоначчи
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(int(input())))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)
# или list1 = [int(input()) for i in range(int(input()))]
max_n = max(list1)
min_n = min(list1)
for i in range(len(list1)):
    if list1[i] == max_n:
        list1[i] = min_n
print(list1)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
def prime(n):
    i = 2
    flag = True
    while i < n // 2 + 1 and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'Yes'
    return 'No'
print(prime(int(input())))

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Решить рекурсией
def f(n):
    if n == 0:
        return ''
    k = int(input())
    return f(n - 1) + str(k)
print(f(int(input())))