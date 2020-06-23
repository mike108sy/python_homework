from itertools import count, cycle
number_begin = int(input('Введите число с которого необходимо начать генерировать целые числа: '))
number_end = int(input('Введите число, на котором необходимо закончить генерацию целых чисел: '))

a = 1

for el in count(number_begin):
    if el > number_end:
        break
    else:
        print(el)

my_list = [i for i in input('Введите значения списка через пробел: ').split()]
n = int(input('Введите количество повторений списка: '))

for el_list in cycle(my_list):
    if a == len(my_list) * n:
        break
    else:
        print(el_list)
        a += 1
