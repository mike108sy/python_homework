with open("file5:5.txt", "w+") as f:
    numbers = [i for i in input('Введите числа для записи в файл через пробел: ').split()]
    numbers_new = []
    for number in numbers:
        number_new = number + '\n'
        numbers_new.append(number_new)
    f.seek(0)
    f.writelines(numbers_new)
    f.seek(0)
    sum_numbers = 0
    numbers_read = f.readlines()
    f.seek(0)
    for i in enumerate(numbers_read):
        number_read = f.readline()
        sum_numbers = sum_numbers + int(number_read)
    print('Сумма введенных в файл чисел равно:', sum_numbers)
