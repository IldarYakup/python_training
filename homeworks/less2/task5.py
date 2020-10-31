"""
5.
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)
while True:
    user_add = input("Добавьте число, которое нужно добавить в список: ")
    try:
        user_add = int(user_add)
        break
    except ValueError:
        print("Вы ввели не правильное значение")
        continue
for idx in my_list:
    if user_add > idx:
        my_list.insert(my_list.index(idx), user_add)
        break
else:
    my_list.append(user_add)
print(my_list)
