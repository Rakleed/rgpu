"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    Задание 1: напишите код на языке Python, позволяющий вычислить
    логические операции, с помощью конкатенации строк, умножения строки
     на число или как-то иначе создайте таблицу и выведите её.

    Задание 2: для данного списка, используя слайсы, обращение к
    элементам по индексу (не используя циклы или условные операторы)
    нужно что-то найти.

    Вариант 4.

"""

# 1 задание
values_2 = ((0, 0), (0, 1), (1, 0), (1, 1))
values_3 = ((0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1),
            (1, 1, 0), (1, 1, 1))


def head_2():
    header = "| A | B | F |"
    under_header = "+ " + "-" * (len(header) - 4) + " +"
    print(under_header)
    print(header)
    print(under_header)


def head_3():
    header = "| A | B | C | F |"
    under_header = "+ " + "-" * (len(header) - 4) + " +"
    print(under_header)
    print(header)
    print(under_header)


def truth_table_5(val):
    result = (val[0] or val[1]) and (not val[2])
    result = int(result)
    line = "| " + str(val[0]) + " | " + str(val[1]) + " | " + str(val[2]) + \
           " | " + str(result) + " |"
    print(line)
    print('+', '-' * (len(line) - 4), '+')


def truth_table_7(val):
    result = (not val[0]) or val[0]  # ((A→B)∧A)↔A∧B = ¬A∨A
    result = int(result)
    line = "| " + str(val[0]) + " | " + str(val[1]) + " | " + str(result) + \
           " |"
    print(line)
    print('+', '-' * (len(line) - 4), '+')


def truth_table_18(val):
    result = (not val[0]) or val[0]  # A∨(B∧C)↔(A∨B)∧(A∨C) = ¬A∨A
    result = int(result)
    line = "| " + str(val[0]) + " | " + str(val[1]) + " | " + str(val[2]) + \
           " | " + str(result) + " |"
    print(line)
    print('+', '-' * (len(line) - 4), '+')


print("1 задание\n\n\n5. F = (A∨B)∧¬C\n")
head_3()
for i in range(len(values_3)):
    truth_table_5(values_3[i])

print("\n\n7. F = ((A→B)∧A)↔A∧B\n")
head_2()
for i in range(len(values_2)):
    truth_table_7(values_2[i])

print("\n\n18. F = A∨(B∧C)↔(A∨B)∧(A∨C)\n")
head_3()
for i in range(len(values_3)):
    truth_table_18(values_3[i])


# 3 задание
lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
       1597, 2584, 4181, 6765, 10946]

print("\n\n\n3 задание\n\n\n16. ", sum(lst[1::2], lst[0]))

car = ("name", " DeLorean DMC-12", "motor_pos", "rear", "n_of_wheels", 4,
       "n_of_passengers", 2, "weight", 1.230, "height", 1.140, "length",
       4.216, "width", 1.857, "max_speed", 177)

print("\n\n22. ", car[::2])
