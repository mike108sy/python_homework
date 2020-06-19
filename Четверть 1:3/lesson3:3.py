def my_func(arg1, arg2, arg3):
        my_sum = arg1 + arg2 + arg3
        number_min = min(arg1, arg2, arg3)
        my_result = my_sum - number_min
        return my_result


qwe = my_func(int(input('Введите число 1: ')), int(input('Введите число 2: ')), int(input('Введите число 3: ')))
print(qwe)
