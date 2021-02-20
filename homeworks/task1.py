#Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""
https://drive.google.com/file/d/1SvKclx9r6yD4OO_QAb7a2uiSh5yJA4lQ/view?usp=sharing
"""
user_arg = int(input("Введите трехзначное число: "))
if user_arg < 1000 and user_arg > 99:
    a = user_arg//100
    b = (user_arg-a*100)//10
    c = user_arg-a*100-b*10
    print(f'сумма трех чисел трехзначного числа  = {a+b+c}')
    print(f'произведение трех чисел трехзначного числа = {a*b*c}')
else:
    print("Вы ввели не 3-ех значное число")
