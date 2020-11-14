"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    title = "Рисование"
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print("Теперь мы рисуем ручкой")
class Pencil(Stationery):
    def draw(self):
        print("Теперь мы рисуем карандашом")
class Handle(Stationery):
    def draw(self):
        print("Теперь мы рисуем маркером")
a = Pen()
b = Pencil()
c = Handle()
a.draw()
b.draw()
c.draw()