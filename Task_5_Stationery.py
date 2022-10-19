"""
Задание 5.
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем публичный атрибут title (название) и публичный метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса: Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    """
    Класс описывает канцелярские принадлежности.
    """
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'{self.title} - Запуск отрисовки')


class Pen(Stationery):
    """
    Класс является подклассом Stationery и описывает множество ручек.
    """
    def draw(self):
        print(f'Ручка {self.title} шариковая')


class Pencil(Stationery):
    """
    Класс является подклассом Stationery и описывает множество карандашей.
    """
    def draw(self):
        print(f'Карандаш {self.title} рисует и на потолке')


class Handle(Stationery):
    """
    Класс является подклассом Stationery и описывает множество маркеров.
    """
    def draw(self):
        print(f'Маркер {self.title} перманентный')


st = Stationery('Фломастер')
st.draw()

pn = Pen('Parker')
pn.draw()

pnsl = Pencil('koh-i-noor')
pnsl.draw()

hndl = Handle('centropen')
hndl.draw()
