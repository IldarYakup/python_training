my_list = []
my_list_2 = []
my_list_3 = []
user_add = input("Введите элемент, который нужно добавить в список: ")
my_list.append(user_add)
n = 0
while True:
    user_ans = input("Добавить элемент в список? \n Y - Да\n N - Нет: ")
    if user_ans.upper() == "Y":
        user_add = input("Введите элемент, который нужно добавить в список: ")
        my_list.append(user_add)
    elif user_ans.upper() == "N":
        break
    else:
        print("Ошибка в ответе")
print(my_list)
while len(my_list) > 1:
    index_1 = my_list[0]
    index_2 = my_list[1]
    my_list_2.insert(n + 1, index_1)
    my_list_2.insert(n, index_2)
    my_list.pop(0)
    my_list.pop(0)
    my_list_3.extend(my_list_2)
    my_list_2.pop(0)
    my_list_2.pop(0)
    if len(my_list) == 1:
        my_list_3.extend(my_list)
    elif len(my_list) < 1:
        break
print(my_list_3)