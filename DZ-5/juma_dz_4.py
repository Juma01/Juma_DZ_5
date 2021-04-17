# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

new_file = []
with open('file_4.txt', 'r', encoding='utf-8') as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + ' ' + i[1])
    print(*new_file)

with open('new_file_4.txt', 'w', encoding='utf-8') as my_file_2:
    my_file_2.writelines(new_file)

# --------------------вариант------------------------------

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('test_new.txt', 'w', encoding='utf-8')as new_file:
    with open('file_4.txt', encoding='utf-8')as my_file:
        new_file.writelines([line.replace(line.split()[0], rus.get(line.split()[0])) for line in my_file])
