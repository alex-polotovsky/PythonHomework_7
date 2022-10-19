"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


from time import sleep


class Car:

    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        if self.speed != speed:
            self.speed = speed
        print(f'Машина {self.name} поехала.')

    def stop(self):
        self.speed = 0
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}.')

    def show_speed(self):
        print(f'скорость: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Вы превысили скорость!')
        print(f'скорость: {self.speed}')

    def answer(self):
        print('Откуда вы берётесь...')


class SportCar(Car):

    def answer(self):
        self.speed = 200
        print('А ты догони...')


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Вы превысили скорость!')
        print(f'скорость: {self.speed}')


class PoliceCar(Car):

    def megafon(self, obj_name):
        print(f'Автомобиль {obj_name} прижмитесь к обочине.')


avto_1 = TownCar(50, 'Yellow', 'Kia Rio', False)
avto_2 = SportCar(110, 'Blue', 'Porsche 911 GT2', False )
avto_3 = PoliceCar(60, 'White', 'Ford Focus', True)

avto_1.go(70)
sleep(3)
avto_1.show_speed()
sleep(1)
avto_3.go(80)
sleep(2)
avto_3.show_speed()
sleep(1)
avto_3.megafon(avto_1.name)
sleep(1)
avto_1.answer()
sleep(2)
avto_1.turn('направо')
sleep(1)
avto_1.stop()
avto_1.show_speed()
sleep(2)
print()
avto_2.go(110)
sleep(1)
avto_2.show_speed()
avto_3.go(80)
sleep(3)
avto_3.show_speed()
sleep(2)
avto_3.megafon(avto_2.name)
sleep(1)
avto_2.answer()
avto_2.go(200)
sleep(1)
avto_2.show_speed()
