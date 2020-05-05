"""
    Автор: Моисеенко Павел, группа № 1, подгруппа № 2.

    Задание: вывести таблицу истинности для and, or, xor, equality.

    Таблица введена с помощью символа "*", int и bool преведены к строкам, и выведены результаты для коньюнкции, дизюнкции, строгой дизъюнкции и эквиваленции.

"""

logical_false = 0
logical_true = 1

delimiter = "*"
space_symbol = " "

header = "* A *" + "* B *" + "* " + " A and B " + "*"

table_width = len(header)

# print (logical_A and logical_B)
print(delimiter * table_width)
print(header)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_true) + " *"
res1 = "*  " + str(int((bool(logical_true) and bool(logical_true)))) + "   *"
print(inp_str + res1)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_false) + " *"
res2 = "*  " + str(int((bool(logical_true) and bool(logical_false)))) + "   *"
print(inp_str + res2)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_true) + " *"
res3 = "*  " + str(int((bool(logical_false) and bool(logical_true)))) + "   *"
print(inp_str + res3)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_false) + " *"
res4 = "*  " + str(int((bool(logical_false) and bool(logical_false)))) + "   *"
print(inp_str + res4)
print(delimiter * table_width)

header = "* A *" + "* B *" + "* " + " A or B " + "*"

# print (logical_A or logical_B)
print("\n" + delimiter * table_width)
print(header)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_true) + " *"
res1 = "*  " + str(int((bool(logical_true) or bool(logical_true)))) + "   *"
print(inp_str + res1)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_false) + " *"
res2 = "*  " + str(int((bool(logical_true) or bool(logical_false)))) + "   *"
print(inp_str + res2)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_true) + " *"
res3 = "*  " + str(int((bool(logical_false) or bool(logical_true)))) + "   *"
print(inp_str + res3)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_false) + " *"
res4 = "*  " + str(int((bool(logical_false) or bool(logical_false)))) + "   *"
print(inp_str + res4)
print(delimiter * table_width)

header = "* A *" + "* B *" + "* " + " A xor B " + "*"

# print (logical_A xor logical_B)
print("\n" + delimiter * table_width)
print(header)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_true) + " *"
res1 = "*  " + str(int((bool(logical_true) ^ bool(logical_true)))) + "   *"
print(inp_str + res1)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_false) + " *"
res2 = "*  " + str(int((bool(logical_true) ^ bool(logical_false)))) + "   *"
print(inp_str + res2)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_true) + " *"
res3 = "*  " + str(int((bool(logical_false) ^ bool(logical_true)))) + "   *"
print(inp_str + res3)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_false) + " *"
res4 = "*  " + str(int((bool(logical_false) ^ bool(logical_false)))) + "   *"
print(inp_str + res4)
print(delimiter * table_width)

header = "* A *" + "* B *" + "* " + " A == B " + "*"

# print (logical_A == logical_B)
print("\n" + delimiter * table_width)
print(header)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_true) + " *"
res1 = "*  " + str(int((bool(logical_true) is bool(logical_true)))) + "   *"
print(inp_str + res1)
print(delimiter * table_width)

inp_str = "* " + str(logical_true) + " ** " + str(logical_false) + " *"
res2 = "*  " + str(int((bool(logical_true) is bool(logical_false)))) + "   *"
print(inp_str + res2)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_true) + " *"
res3 = "*  " + str(int((bool(logical_false) is bool(logical_true)))) + "   *"
print(inp_str + res3)
print(delimiter * table_width)

inp_str = "* " + str(logical_false) + " ** " + str(logical_false) + " *"
res4 = "*  " + str(int((bool(logical_false) is bool(logical_false)))) + "   *"
print(inp_str + res4)
print(delimiter * table_width)
