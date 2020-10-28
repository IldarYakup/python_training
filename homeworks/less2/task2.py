my_list = []
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




my_list2 = ['1', '2', '3', '4']
tuple(my_list2)
for el in my_list2:
    my_list2.append(el * 2)
print(my_list2)