user_number = input("Задайте число n, которое вставится в формулу n + nn + nnn: ")
formula = int(str(user_number)) + int(str(user_number + user_number)) + int(str(user_number + user_number + user_number))
print(str(user_number) + "+" + str(user_number + user_number) + "+" + str(user_number + user_number + user_number) + "=" + str(formula))