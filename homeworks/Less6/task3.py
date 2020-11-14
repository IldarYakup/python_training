"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": "", "bonus": ""}

class Position(Worker):

    def get_full_name(self):
        print(f'{self.position} - {self.surname} {self.name}')

    def get_total_income(self):
        print(f'доход с учетом премии: {self._income["wage"] + self._income["bonus"]} тыс. руб.')
person_1 = Position()
person_1.name = "Владимир"
person_1.surname = "Зеленский"
person_1.position = "Президент"
person_1._income = {"wage": 100000, "bonus": 25000}
person_1.get_full_name()
person_1.get_total_income()