def my_func(a):
    my_list = []
    for z in range(len(a)):
        a[z] = int(a[z])
    my_sum1 = 0
    for i in a:
        my_sum1 += i
    my_list.append(my_sum1)
    return my_sum1

my_resultlist = []
while True:
    my_resulte = my_func([i for i in input('Введите значения списка через пробел: ').split()])
    my_resultlist.append(my_resulte)
    print('За весь цикл вы ввели следующие суммы чисел:', my_resultlist)
    print('Сумма введенных чисел за весь цикл равна:', sum(my_resultlist))
    if input('Нажмите ENTER для продолжения суммирования чисел или Q для выхода! ').upper() == 'Q':
        break
