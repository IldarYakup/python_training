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
my_f = open("ForTask4.txt", "r", encoding="UTF-8")
read_file = my_f.read()
list = read_file.split()
print(list)
my_dict = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
for i, e in enumerate(list):
    if e in my_dict:
        list[i] = my_dict[e]
i = 0
while True:
    print(list[i:[i+2]])
    i += 2
"""output = " "
output_new = output.join(list)
print(output_new)"""
"""for a, b, c in output_new:
    str = a + b + c
    print(str)
"""