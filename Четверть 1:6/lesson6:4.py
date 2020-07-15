#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, speed, name, color, is_police):
        self.speed = speed
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        print('Машина повернула (куда)')

    def show_speed(self, speed_now):
        print('Текущая скорость автомобиля {}'.format(speed_now))

class TownCar(Car):

    def __init__(self, speed, name, color, is_police, height):
        super().__init__(speed, name, color, is_police)
        self.height = height
        self.is_police = False

    def show_speed(self, speed_now):
        print('Превышение скорости') if speed_now > 60 else print('Скорость не превышена')


class SportCar(Car):

    def __init__(self, speed, name, color, is_police, maxspeed):
        super().__init__(speed, name, color, is_police)
        self.maxspeed = maxspeed
        self.is_police = False


class WorkCar(Car):

    def __init__(self, speed, name, color, is_police, company):
        super().__init__(speed, name, color, is_police)
        self.company = company
        self.is_police = False

    def show_speed(self, speed_now):
        print('Превышение скорости') if speed_now > 40 else print('Скорость не превышена')


class PoliceCar(Car):

    def __init__(self, speed, name, color, is_police, police_number):
        self.police_number = police_number
        super().__init__(speed, name, color, is_police)
        self.is_police = True


my_car = TownCar(80, 'mazda', 'red', False, 1.2)
print(my_car.name)
my_car.go()
my_car.stop()
my_car.turn()
print(my_car.show_speed(int(input('Введите текущую скорость автомобиля:'))))

my_car = WorkCar(80, 'ferrari', 'red', False, 'Rostelecom')
print(my_car.name)
my_car.go()
my_car.stop()
my_car.turn()
print(my_car.show_speed(int(input('Введите текущую скорость автомобиля:'))))

my_car = SportCar(80, 'honda', 'red', False, 300)
print(my_car.name)
my_car.go()
my_car.stop()
my_car.turn()
print(my_car.show_speed(int(input('Введите текущую скорость автомобиля:'))))
