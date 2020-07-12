#Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.surname, self.name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


position1 = Position('Ivan', 'Ivanov', 'director', 100000, 50000)
print('Полное имя сотрудника:', position1.get_full_name())
print('Доход сотрудника с учетом премии:', position1.get_total_income())
