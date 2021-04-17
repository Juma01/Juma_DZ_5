# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_file = open("test.txt", "r", encoding='UTF-8')
content = my_file.read()
print(f"Содержимое файла: \n\t {content.title()}")
my_file = open("test.txt", "r")
content = my_file.readlines()
print(f"Количество строк в файле - {len(content)}")
my_file = open("test.txt", "r")
content = my_file.readlines()
for el in range(len(content)):
    print(f"Количество символов в {el + 1} - ой строке {len(content[el])}")
my_file = open("test.txt", "r")
content = my_file.read()
content = content.split()
print(f"Общее количество слов - {len(content)}")
my_file.close()

# ----------------------------------вариант---------------------------

with open('test.txt', encoding='utf-8') as file:
    my_file = file.readlines()
    for idex, value in enumerate(my_file, 1):
        num_words = len(value.split())
        print(f"Строка {idex} содержит {num_words} слов")
