"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    ИСР 2.2. Задание: дополнить программу «Калькулятор» декоратором,
    сохраняющим выполняемые действия в файл-журнал.

"""


def save_result_in_file(func):
    try:
        file_handler = open("log.txt", "a")
        file_handler.write(func())
    except IOError:
        print("An IOError has occurred!")
    except UnboundLocalError:
        print("Непредвиденная ошибка.")
    finally:
        file_handler.close()


@save_result_in_file
def calc():
    string_write_buff = ""
    is_work = True
    while is_work:
        string_calc = input("Введите выражение в форме <число><пробел><мат.оп"
                            "ерация><пробел><число> (или «q» для выхода): ")
        if string_calc.lower() == "q":
            break
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
    try:
        calc()
    except:
        print("Not callable.")
