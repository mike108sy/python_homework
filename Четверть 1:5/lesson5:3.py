with open("file5:3.txt", "r+") as f:
    surname = ' '
    while True:
        surname = input('Введите фамилию сотрудника и нажмите "Enter": ')
        if surname == '':
            break
        salary = input('Введите заработную плату сотрудника и нажмите "Enter": ')
        print(surname, salary, file=f)
        file = f.read()
    f.seek(0)
    lines = f.readlines()
    salary_full = 0
    person_count = 0
    for line in lines:
        person_count += 1
        line_correct = line.strip('\n')
        ind = line.index(' ')
        salary_find = int(line_correct[ind:])
        surname_find = line_correct[:ind]
        salary_full += salary_find
        if salary_find < 20000:
            print(surname_find)
salary_medium = salary_full / person_count
print('Средняя заработная плата сотрудников в компании: ', '%.2f' % salary_medium)
