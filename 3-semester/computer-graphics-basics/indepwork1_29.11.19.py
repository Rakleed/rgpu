from tkinter import *
import random


def make_cells():
    wd = 40
    hg = 20
    for i in range(6):
        color = '#' + hex(random.randint(0, 255))[2:] + hex(random.randint(0, 255))[2:] + hex(random.randint(0, 255))[2:]
        if len(color) < 7:
            color = color + '0' * (7-len(color))
        Canvas(root, width=wd, height=hg, bg=color).place(x=290, y=20 + i*50)
        Label(root, text=color, width=15).place(x=30, y=20 + i*50)


root = Tk()
root.title('Цвет ячейки')
root.geometry('400x400')
root.resizable(width=False, height=False)
make_cells()
Button(root, text='Обновить цвета', command=make_cells).place(x=150, y=330)

root.mainloop()
