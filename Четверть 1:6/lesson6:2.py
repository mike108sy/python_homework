#Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

#Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, length, _width):
        self.massa1 = 25
        self.tolshina = 5
        self.length = length
        self.width = _width

    def material(self):
        mass = self.length * self.width * self.massa1 * self.tolshina / 1000
        return mass


a = Road(int(input('Введите длину дороги: ')), int(input('Введите ширину дороги: ')))
print('Масса асфальта, необходимого для покрытия всего дорожного полотна:', a.material(), 'т')



