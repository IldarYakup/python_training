"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    speed = ""
    color = ""
    name = ""
    is_police = False
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Авто поехало")

    def stop(self):
        print("Авто остановилась")

    def turn(self, direction):
        print(f'Авто повернуло {direction}')

    def show_speed(self, speed):
        print(f'Текущая скорость {speed} км/ч')

    def police(self, is_police):
        if is_police == False:
            print("Авто не относится к полицескому экипажу")
        else:
            print("Авто из полицеского экипажа")



class TownCar(Car):
    def show_speed(self, speed):
        print(f'Текущая скорость {speed} км/ч')
        if speed > 60:
            print('Авто превышает скорость')

class SportCar(Car):
    def go(self):
        print("Не поехала, а погнала")

class WorkCar(Car):
    def show_speed(self, speed):
        print(f'Текущая скорость {speed} км/ч')
        if speed > 40:
            print('Авто превышает скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police != is_police

car1 = SportCar(120, 'Красный', 'Lamborghini Diablo', False)
car2 = WorkCar(60, 'Черный', 'Volvo CX60', False)
car3 = TownCar(50, 'Желтый', 'ПАЗ', False)
car4 = PoliceCar(110, 'Бело-cиний', 'Ford Focus', True)

print(car1.color, car1.name)
car1.go()
car1.show_speed(145)
print("")
print(car2.color, car2.name)
car2.go()
car2.turn("налево")
car2.show_speed(62)
print("")
print(car3.color, car3.name)
car3.go()
car3.show_speed(59)
car3.police(False)
print("")
print(car4.color, car4.name)
car3.go()
car3.show_speed(59)
car3.police(True)