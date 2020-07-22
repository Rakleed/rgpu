"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 2.1. Задание: разработать прототип программы «Калькулятор»,
    позволяющую выполнять базовые арифметические действия и функцию
    обертку, сохраняющую название выполняемой операции, аргументы и
    результат в файл (без использования '@').

"""


def save_result_in_file(what_to_write):
    try:
        file_handler = open("log.txt", "a")
        file_handler.write(what_to_write)
    except IOError:
        print("An IOError has occurred!")
    except:
        print("Непредвиденная ошибка.")
    finally:
        file_handler.close()


def calc():
    string_write_buff = ""
    is_work = True
    while is_work:
        string_calc = input("Введите выражение в форме <число><пробел><мат.оп"
                            "ерация><пробел><число> (или «q» для выхода): ")
        if string_calc.lower() == "q":
            save_result_in_file(string_write_buff)
            exit()
        list_from_user_string = string_calc.split()
        if list_from_user_string[1] == "+":
            result = float(list_from_user_string[0]) + \
                     float(list_from_user_string[2])
        elif list_from_user_string[1] == "-":
            result = float(list_from_user_string[0]) - \
                     float(list_from_user_string[2])
        elif list_from_user_string[1] == "*":
            result = float(list_from_user_string[0]) * \
                     float(list_from_user_string[2])
        elif list_from_user_string[1] == "/":
            result = float(list_from_user_string[0]) / \
                     float(list_from_user_string[2])
        else:
            print("Error.")
        try:
            string_write_buff += string_calc + " = " + str(result) + "\n"
        except UnboundLocalError:
            print("Ошибка передачи данных.")
        print(string_calc + " = " + str(result))
    return string_write_buff


if __name__ == "__main__":
    calc()
