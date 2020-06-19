def division(arg1, arg2):
        my_div = arg1 / arg2
        return my_div

while True:
    try:
        my_result = division(int(input('Введите делимое: ')), int(input('Введите делитель: ')))
        print(my_result)
        break
    except ZeroDivisionError:
        print('Деление на ноль!')
    except ValueError:
        print('Введено не число')
