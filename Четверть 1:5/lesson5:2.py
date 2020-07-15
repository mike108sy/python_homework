with open("file5:2.txt", "a+") as f:
    line = ' '
    while True:
        line = input('Введите текст для записи и нажмите "Enter": ')
        if line == '':
            break
        print(line, file=f)
        file = f.read()
    f.seek(0)
    lines = f.readlines()
    lines_count = 0
    for line_number, i in enumerate(lines):
        lines_count += 1
        words_line = i.count(' ')
        if i != '\n':
            print('Количество слов в', line_number+1, 'строке: ', words_line+1)
        else:
            print('Количество слов в', line_number+1, 'строке: ', 0)
    print('Количество строк в файле "file5:2.txt": ', lines_count)
