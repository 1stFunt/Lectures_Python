# Задача с планетами. Главное отсечь одинаковые числа и найти наибольшее произведение чисел.
def find(orbits):
    list_of_elliptical_orbits = [i for i in orbits if i[0] != i[1]]
    list_of_areas = [i[0] * i[1] for i in list_of_elliptical_orbits]
    max_area_index = [i for i in range(len(orbits)) if orbits[i][0] * orbits[i][1] == max(list_of_areas)]
    return orbits[max_area_index[0]]
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
orbits = [(1, 3), (4, 3), (7, 2), (6, 6), (2.5, 10)]
print(*find(orbits))
# вариант решения с lambda
def find(orbits):
    return max(orbits, key = lambda x: (x[0] != x[1]) * x[0] * x[1])
orbits = [(1, 3), (4, 3), (7, 2), (6, 6), (2.5, 10)]
print(*find(orbits))

# ещё задачка
def same_by(func, collection):
    return len(list(filter(func, collection))) == 0     # x % 2 равно 1 когда число нечетное, 1 - это True, а функция filter возвращает True
                                                        # В данной задаче всё что вернёт filter в функции same_by не будет равнятся 0 по условию,            
values = [0, 2, 10, 6]                                  # если попадётся нечётное число
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')