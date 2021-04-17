# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
my_f = open("salary.txt", "r")
content = my_f.read()
print(f"Содержимое файла: \n {content}")
sal = []
mini = []
my_list = content.split('\n')
for i in my_list:
    i = i.split()
    if float(i[1]) < 20000:
        mini.append(i[0])
    sal.append(i[1])
print(f"Оклад меньше 20.000 {mini}, Средний оклад {sum(map(float, sal)) / len(sal)}")
my_f.close()