# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""
https://drive.google.com/file/d/1S61A6uOFO3_YSilFb_aNRE7skTcVE5N3/view?usp=sharing
"""
print('Программа для определения среднего числа из трех заданных чисел')
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if c < a < b or b < a < c:
    print(f' среднее число из чисел {a}, {b}, {c} является число {a}')
if a < b < c or c < b < a:
    print(f' среднее число из чисел {a}, {b}, {c} является число {b}')
if a < c < b or b < c < a:
    print(f' среднее число из чисел {a}, {b}, {c} является число {c}')