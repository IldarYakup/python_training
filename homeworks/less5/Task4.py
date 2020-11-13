"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
list= []
my_f = open("ForTask4.txt", "r", encoding="UTF-8")
read_file = my_f.readline()
for line in read_file:
    if len(read_file.split()) == 0:
        break
    list.append(read_file.split())
    read_file = my_f.readline()
my_f.close()
my_dict = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
for el in list:
    for i, e in enumerate(el):
        if e in my_dict:
            el[i] = my_dict[e]
output_new = ""
with open('task4.txt', 'w', encoding='utf-8') as new:
    for idx, el in enumerate(list):
        output_new += (" ".join(list[idx]) + "\n")
    new.write(output_new)