user_second = input("Введите количество секунд которые нужно перевести: ")
hours = int(user_second) // 3600
minutes = (int(user_second) % 3600) // 60
seconds = ((int(user_second) % 3600) % 60) % 60
print('Ваше количество секунд = ' + user_second + ', что равно {0} ч. {1} мин. {2} сек., или же {0}:{1}:{2}'.format(hours, minutes, seconds) )