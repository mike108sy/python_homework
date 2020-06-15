x = int(input('Введите целое положительное число: '))
x = str(x)
count = len(x)
y = int(count)
print('Количество цифр в числе:',y)
n = 0
x1 = int(x[n])
if count == 1:
    print(x1)
else:
    print('Промежуточные результаты поиска на каждой итерации цикла:')
    while n < y:
        x2 = int(x[n])
        if x1 > x2:
            x1 = x1
        else:
            x1 = x2
        print(x1)
        n = n + 1
print('Самая большая цифра в числе:', x1)
