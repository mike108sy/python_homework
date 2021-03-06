#Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.

#Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

#Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

#Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

#Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

#В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.

#Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

#Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.

#Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

#Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Kletka:

    def __init__(self, counts):
        self.counts = int(counts)

    def __add__(self, other):
        summa = self.counts + other.counts
        return summa

    def __sub__(self, other):
        if self.counts > other.counts:
            vichitanie = self.counts - other.counts
        else:
            vichitanie = 'Невозможно выполнить операцию, количество ячеек в первой клетке меньше, чем во второй'
        return vichitanie

    def __mul__(self, other):
        proizvedenie = self.counts * other.counts
        return proizvedenie

    def __truediv__(self, other):
        delenie = round(self.counts) // round(other.counts)
        return delenie

    def make_order(self, n):
        order = ''
        for i in range(1, self.counts+1):
            order += '*'
            if i % n == 0:
                order += '\n'
        return order


kletka1 = Kletka(4)
kletka2 = Kletka(10.5)
print(kletka1 + kletka2)
print(kletka1 - kletka2)
print(kletka2 - kletka1)
print(kletka1 * kletka2)
print(kletka1 / kletka2)
print(kletka2 / kletka1)
print('Ячейки клетки по рядам:', '\n', kletka1.make_order(3))
