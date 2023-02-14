# Функция
def sum_numbers(n, y='Hello'):    # y = по умолчанию, если нет второго аргумента
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
print(sum_numbers(5))

def sum_str(*args):     # * - неограниченное кол-во аргументов
    res = ''
    for i in args:
        res += i
    return res
print(sum_str('h', 'e', 'l', 'l', 'o'))

# Вызов модулей с функциями (импортирование)
import modul
print(modul.max(1, 9))

# Другие варианты вызова модулей
from modul import max  # если вместо max поставить * , то импортируются все функции из модуля
print(max(1, 9))

# Вариант с сокращением имени модуля
import modul as m
print(m.max(1, 9))

# РЕКУРСИЯ
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# Быстрая сортировка + рекурсия
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]    # Первый элемент известен, поэтому от 1 до - [1:]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)    # pivot - заключаем в скобки, чтоб перевести из int в list
print(quick_sort([14, 4, 5, 7, 9, 8, 10]))

# Сортировка слиянием (смотреть суть на картинке .png)
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list_1 = [8, 6, 7, 4, 88, 34, 76, 43]
merge_sort(list_1)
print(list_1)