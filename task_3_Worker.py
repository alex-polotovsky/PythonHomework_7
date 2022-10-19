"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:
    """
    Класс представляет базу данных сотрудников.
    """
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    """
    Класс позволяет получить ФИО сотрудника, его должность и доход.
    """
    def get_full_name(self):
        """
        Функция возвращает полное имя человека.
        :param self: Access the attributes and methods of the class
        :return: The concatenation of the name and surname attributes
        """
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        """
         Функция возвращает общий доход сотрудника компании.
        :param self: Access the instance attributes and methods of the class
        :return: The sum of the incomes in the dictionary
        """
        return sum(self._income.values())

    def __str__(self):
        return f'{self.name} {self.surname}, {self.position}, ' \
               f'доход: {sum(self._income.values())}'


employee_1 = Position('Иван', 'Петров', 'инженер', 70, 30)
employee_2 = Position('Пётр', 'Васильев', 'рабочий', 100, 50)

print(employee_1.get_full_name())
print(f'Полный доход: {employee_1.get_total_income()}')
print()
print(employee_1)
print(employee_2)
