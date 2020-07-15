with open("test.txt", "w+") as f:
    line = ' '
    while line != '':
        line = input('Введите текст для записи и нажмите "Enter": ')
        print(line, file=f)
        file = f.read()
