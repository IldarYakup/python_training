user_second = input("Введите количество секунд которые нужно перевести: ")
hours = int(user_second) // 3600
minutes = (int(user_second) % 3600) // 60
seconds = ((int(user_second) % 3600) % 60) % 60
print('Ваше количество секунд = ' + user_second + ', что равно {0} Часов {1} минутам {2} секундам, или же {0}:{1}:{2}'.format(hours, minutes, seconds) )