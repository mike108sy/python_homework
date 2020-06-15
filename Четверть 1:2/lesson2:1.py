my_list = [1, 3, 'as23', True, 23.5]
print(type(my_list))
n = 0
for i in my_list:
        print('Тип', n, 'элемента списка:', type(my_list[n]))
        n += 1
