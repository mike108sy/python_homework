def int_func(word):
    my_list = list(word)
    print(my_list)
    for i in range(len(my_list)):
        my_list[i] = my_list[i].title()
    s = ' '
    my_resulte = s.join(my_list)
    return my_resulte


print(int_func([i for i in input('Введите значения списка через пробел: ').split()]))
