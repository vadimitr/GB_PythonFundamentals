# 4. Реализуйте базовый класс Car.
# У данного класса должны быть
# - атрибуты: speed, color, name, is_police (булево).
# - методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем {direction}')
        else:
            print('Не можем повернуть - мы стоим на месте')

    def show_speed(self):
        print(f'Скорость {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Скорость {self.speed}! Превышение скорости на {self.speed - 60} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Скорость {self.speed}! Превышение скорости на {self.speed - 40} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True

def car_test(vehicle):
    print(f"Тест {'полицейского' if vehicle.is_police else 'гражданского'} автомобиля {vehicle.name}, цвет {vehicle.color}")
    vehicle.go(40)
    vehicle.show_speed()
    vehicle.turn('направо')
    vehicle.stop()
    vehicle.show_speed()
    vehicle.turn('налево')
    vehicle.go(60)
    vehicle.show_speed()
    vehicle.go(120)
    vehicle.show_speed()
    vehicle.stop()
    print("Тест окончен", end="\n\n")

kia = Car('терракотовый', 'Kia Seed', False)
car_test(kia)

vesta = TownCar('белый', 'Lada Vesta')
car_test(vesta)

marusya = SportCar('красный', 'Маруся')
car_test(marusya)

largus = WorkCar('красный', 'Lada Largus')
car_test(largus)

taurus = PoliceCar('черно-белый', 'Ford Taurus')
car_test(taurus)