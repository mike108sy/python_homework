my_nomer = int(input('Введите номер месяца от 1 до 12: '))
number = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
my_index = number.index(my_nomer)
print(my_index)
if my_index <= 2:
    print('Зима')
elif my_index <= 5:
    print('Весна')
elif my_index <= 8:
    print('Лето')
else:
    print('Осень')
