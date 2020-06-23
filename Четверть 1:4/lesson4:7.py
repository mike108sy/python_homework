from math import factorial


def fact(n):
    for i in range(1, n+1):
        res = factorial(i)
        yield res

n = int(input('Введите число n, на котором остановится расчет факториалов чисел: '))
print(fact(n))

for res in fact(n):
    print(res)
