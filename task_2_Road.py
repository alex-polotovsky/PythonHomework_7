"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    """
    Класс определяет параметры асвальтового покрытия дороги.
    """
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, udmass, thikness):
        """
        Функция вычисляет массу асфальта, необходимого для покрытия им дороги.
        Она принимает два аргумента: udmass и thikness.
        Функция возвращает общую массу требуемого асфальта.

        :param self: Represent the instance of the class
        :param udmass: Удельная масса асфальта (1м^2 дороги толщиной 1см
        :param thikness: Необходимая толщина покрытия
        :return: The mass of asphalt required to cover the road
        """
        self.udmass = udmass
        self.thikness = thikness
        return self._length * self._width * self.udmass * self.thikness


my_road = Road(5000, 20)

print('Масса асфальта: ', my_road.mass_of_asphalt(25, 0.05))
print(my_road.udmass, my_road.thikness)
