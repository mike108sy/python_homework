def my_func(x, pow):
    rez = 1
    if pow == 0:
        return 1
    elif pow > 0:
        while pow > 0:
            rez = rez * x
            pow = pow - 1
        return rez
    else:
        while pow < 0:
            rez = rez * x
            pow = pow + 1
        return 1/rez


print('Результат от возведения числа в степень: ', my_func(int(input('Введите действительное положительное число: ')), int(input('Введите степень: '))))
