"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

my_f = open("ForTask3.txt", "r", encoding="UTF-8")
read_file = my_f.read()
list = read_file.split()
dict = {list[ind] : list[ind + 1] for ind in range(0, len(list), 2)}
sum = 0
surname = 0
for key, value in dict.items():
    value = int(value)
    sum += value
    surname += 1
    if value < 20000:
        print(f'Сотрудник с фамилией {key} зарабатывает меньше 20 тыс. руб')

print(f'Средняя величина дохода сотрудников равна {sum/surname/1000} тыс. руб')