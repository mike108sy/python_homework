x = int(input('Введите х: '))
y = int(input('Введите y: '))
summa_0 = x + y
print('x =', x)
print('y =', y)
summa_1 = int(input('Сколько будет x+y: '))
if summa_1 == x + y:
    print('Правильно')
else:
    print('Неправильно!')
print('')
print('Результаты выполнения задания:')
print('Ваш ответ:', summa_1, 'Правильный ответ:', summa_0)
