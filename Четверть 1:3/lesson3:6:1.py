def int_func(word):
    my_list = list(word)
    print(my_list)
    my_list[0] = my_list[0].title()
    s = ''
    my_resulte = s.join(my_list)
    return my_resulte


print(int_func(input('Введите слово: ')))
