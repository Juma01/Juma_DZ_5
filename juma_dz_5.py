# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summa():
    try:
        with open("file_5.txt", "w+") as file_obj:
            line = input("Введите цифры через пробел \n")
            file_obj.writelines(line)
            my_num = line.split()
            print(sum(map(int, my_num)))
    except IOError:
        print("Ошибка")
    except ValueError:
        print("Неправельно набран номер.Ошибка ввода-вывода")


summa()
