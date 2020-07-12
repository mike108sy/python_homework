#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

#Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

#Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clouse:
    material_common = []

    def __init__(self, title):
        self.title = title


    def rashod_tkani(self):
        rashod_common = sum(Clouse.material_common)
        return rashod_common


class MyAbstractClass(ABC):
        @abstractmethod
        def size_material(self):
            pass


class Palito(Clouse, MyAbstractClass):

    def __init__(self, v, title):
        super().__init__(title)
        self.v = v

    @property
    def my_method(self):  # позволит обращаться к атрибуту напрямую через точку, минуя функции
        return f"Параметры, переданные в класс:" \
               f" {self.v}"

    @property          # определяем свойства размера пальто (атрибута класса) для вызова сетера и установки свойств по наим еньшему и наиболшему значению
    def v(self):
        return self.__v

    # сеттер для создания свойств
    @v.setter
    def v(self, v):
        if v < 1:
            self.__v = 1
        elif v > 10:
            self.__v = 10
        else:
            self.__v = v

    def get_palito_size(self):
        return f"Размер пальто:{str(self.v)}"

    def size_material(self):
        size_m = self.v / 6.5 + 0.5
        Clouse.material_common.append(size_m)
        return size_m




class Kostum(Clouse, MyAbstractClass):

    def __init__(self, h, title):
        super().__init__(title)
        self.h = h

    @property
    def my_method(self):                # позволит обращаться к атрибуту напрямую через точку, минуя функции
        return f"Параметры, переданные в класс:" \
               f" {self.h}"

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        if h < 1:
            self.__h = 1
        elif h > 10:
            self.__h = 10
        else:
            self.__h = h

    def get_kostum_size(self):
        return f"Размер костюма:{str(self.h)}"

    def size_material(self):
        size_m = 2 * self.h + 0.3
        Clouse.material_common.append(size_m)
        return size_m

class Maika(Clouse, MyAbstractClass):

    def __init__(self, j, title):
        super().__init__(title)
        self.j = j

    def size_material(self):
        size_m = 2 * self.j + 0.3
        Clouse.material_common.append(size_m)
        return size_m



clouse = Clouse('magazine')
maika = Maika(50, 'maika_yellow')
palito = Palito(100, 'palito_white')
print('Расход ткани на {}:'.format(palito.title), palito.size_material())
costum = Kostum(100, 'costum_white')
print('Расход ткани на {}:'.format(costum.title), costum.size_material())
costum2 = Kostum(150, 'costum_red')
print('Расход ткани на {}:'.format(costum2.title), costum2.size_material())
print('Общий расход ткани на всю одежду: ', clouse.rashod_tkani())
print(palito.get_palito_size())
print(costum.h)
print(costum.get_kostum_size())
