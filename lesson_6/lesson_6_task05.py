# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Я рисую {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Я рисую {self.title} ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Я рисую карандашем {self.title}")

class Handle(Stationery):
    def draw(self):
        print(f"Я рисую {self.title} маркером")

stationery = Stationery('красками')
stationery.draw()

pen = Pen('шариковой')
pen.draw()

pencil = Pencil('Koh-i-noor')
pencil.draw()

handle = Handle('перманентным')
handle.draw()