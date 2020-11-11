"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

my_f = open("ForTask2.txt", "r")
content = my_f.readlines()
for idx, word in enumerate(content, 1):
    word = word.count(" ")
    print(f'В строке под №{idx}, {word+1} слов')
my_f.close()
