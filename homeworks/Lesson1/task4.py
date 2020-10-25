user_number = abs(int(input("Введите целое положительное число, чтобы программа определила самую больщую цифру в числе: ")))
max_number = user_number % 10
while user_number >= 1:
    user_number = user_number // 10
    if user_number % 10 > max_number:
        max_number = user_number % 10
    if user_number > 9:
        continue
    else:
        print("Максимальное цифра - ", max_number)
        break