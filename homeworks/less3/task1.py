"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""
print("Для реализации функции деления числа А на число B,")
def my_func (a, b):
    result = a/b
    return result
while True:
    user_arg1 = input("Введите числовое значение числа А: ")
    user_arg2 = input("Введите числовое значение числа В: ")
    try:
        user_arg1 = int(user_arg1)
        user_arg2 = int(user_arg2)
    except ValueError:
        print("Значение А и/(или) В не является числом")
        continue
    try:
        my_func(user_arg1, user_arg2)
    except ZeroDivisionError:
        print("Извините, но на ноль делить нельзя")
        continue
    break
print(my_func(user_arg1, user_arg2))
