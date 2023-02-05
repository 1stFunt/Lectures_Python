# n = int(input('Введите кол-во км, которе машина проходит за день: '))
# m = int(input('Введите общий пробег: '))
# print((n + m - 1) // n)

# a = int(input('Введите кол-во учеников в 1ом классе: '))
# b = int(input('Введите кол-во учеников во 2ом классе: '))
# c = int(input('Введите кол-во учеников в 3ем классе: '))
# a1 = (a+1)//2
# b1 = (b+1)//2
# c1 = (c+1)//2
# print(a1+b1+c1)

# a = int(input())
# b = int(input())
# if a == b:
#     print(0)
# else:
#     print(a+b-1)

year = int(input('Введите год: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'Год {year} является високосным.')
else:
    print(f'Год {year} не является високосным.')