#Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.

#Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

#Примеры матриц вы найдете в методичке.

#Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

#Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

#Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:

    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return f'{self.my_matrix}'

    def __add__(self, other):
        matrix_new = []
        if len(self.my_matrix) == len(other.my_matrix):
            for i, x in zip(self.my_matrix, other.my_matrix):
                if len(i) != len(x):
                    print('Матрицы разных размеров. Сложение невозможно!!!')
                    break
                matrix_new_stroka = []
                for element1, element2 in zip(i, x):
                    element_new = element1 + element2
                    matrix_new_stroka.append(element_new)
                matrix_new.append(matrix_new_stroka)
        else:
            print('Матрицы разных размеров. Сложение невозможно!!!')

        return matrix_new


matrix1 = Matrix(((31, 22), (37, 43), (51, 86)))
matrix2 = Matrix(((3, 5), (2, 4), (-1, 64)))
matrix3 = Matrix(((3, 5), (2, 4)))
print(matrix1.my_matrix)
print(matrix2.my_matrix)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
print(matrix1 + matrix3)
