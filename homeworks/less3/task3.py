"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""
def my_func(*args):
    list = [a, b, c]
    list.pop(list.index(min(list)))
    result = list[0] + list[1]
    return result
while True:
    a = input("Введите число A: ")
    b = input("Введите число B: ")
    c = input("Введите число C: ")
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        break
    except ValueError:
        print("Нужно вводить числа")
        continue
print(my_func(a, b, c))