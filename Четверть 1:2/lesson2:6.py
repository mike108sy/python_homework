counts_product = int(input('Введите количество товаров, которое вы хотите ввести на склад: '))
#my_tuple = tuple('')
#print(my_tuple)
#m_y_dict = {'название': 1, 'цена': 2, 'количество': 3, 'ед.': 4}
my_set = ()
for i in range(counts_product):
    name = input('Введите название товара i: ')
    value = input('Введите цену товара i: ')
    counts = input('Введите количество товара i: ')
    unit = input('Введите единицу измерения товара i: ')
    my_dict = {'название': name, 'цена':  value, 'количество': counts, 'ед.': unit}
    print(my_dict)
    my_set.add(my_dict)
print(my_set)

#1 час ночи. не доделал скрипт!!!