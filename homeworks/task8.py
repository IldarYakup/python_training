#Определить, является ли год, который ввел пользователь, високосным или не високосным.
"""
https://drive.google.com/file/d/1LdTnbGl1oE9okqEe9Yksfq6s6wVooe5W/view?usp=sharing
"""

print("Программа для определения, является ли год, указанный пользователем, высокосным")
user_arg = int(input("Введите год, для определения: "))
if user_arg%4==0:
    print(f'{user_arg} год является высокосным')
elif user_arg%100==0 and user_arg%400!=0 and user_arg>1582:
    print(f'{user_arg} год не является высокосным')
elif user_arg<1582 or (user_arg%400==0 and user_arg>1582):
    print(f'{user_arg} год является высокосным')
else:
    print(f'{user_arg} год не является высокосным')


