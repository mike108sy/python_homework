#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

#Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from datetime import datetime
from datetime import timedelta
import time
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = (('Red', 5), ('Yellow', 2), ('Green', 4))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(подождите {} секунд)'.format(sec))
            start_time = datetime.now()
            deadline_1 = datetime(1, 1, 1, 1, 1, 0)
            deadline_2 = datetime(1, 1, 1, 1, 1, 1)
            deadline = deadline_2 - deadline_1
            time_sleep = timedelta(seconds=sec)
            time.sleep(sec)
            stop_time = datetime.now()
            print('время выполнения операции:', stop_time - start_time)
            if stop_time - start_time > time_sleep + deadline:
                print('время работы светофора некорректное')
                break
            else:
                print('время работы светофора корректное (погрешность по времени вывода сигнала светофора не более 1 секунды)')

a = TrafficLight()
a.running()
