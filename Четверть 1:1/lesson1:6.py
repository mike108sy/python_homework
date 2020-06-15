a = int(input('Дистанция бега в первый день: '))
b = int(input('Какую общую дистанцию хотите достигнуть: '))
dist = a
day = 1
day_str = str(day)
print('Результат:')
print(day_str+'-й день:', dist)
while dist < b:
        dist = dist + (dist / 100 * 10)
        day = day + 1
        day_str = str(day)
        print (day_str+'-й день:', dist)
b_str=str(b)
print('Ответ: на '+day_str+'-й день спортсмен достиг результата - не менее '+b_str+' км')
