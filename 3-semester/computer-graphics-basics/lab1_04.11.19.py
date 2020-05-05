from tkinter import *


def button_clicked():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        label_sum.config(text=str(x + y))
    except ValueError:
        label_sum.config(text="Ошибка. Введите цифры.")


root = Tk()
root.title("Сложение двух чисел")
root.geometry('300x110')

entry_1 = Entry(root)
entry_1.pack()
label_plus = Label(root, text="+")
label_plus.pack()
entry_2 = Entry(root)
entry_2.pack()
button = Button(root, text='=', command=button_clicked)
button.pack()
label_sum = Label(root, text="")
label_sum.pack()

root.mainloop()
