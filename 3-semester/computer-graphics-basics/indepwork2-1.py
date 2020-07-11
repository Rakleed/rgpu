from tkinter import *

WD = 500
ZR = WD / 2
KF = 10
MAIN_TR = [(-15, -10), (0, 15), (15, -10)]


def dec_to_scr(cords: tuple):
    return cords[0] * KF + ZR, ZR - cords[1] * KF


def axis():
    cnvs.create_line(0, 250, 500, 250, arrow=LAST)
    cnvs.create_line(250, 500, 250, 0, arrow=LAST)
    cnvs.create_text(WD - 20, ZR + 20, text='X')
    cnvs.create_text(ZR - 20, 20, text='Y', )
    vals = [i for i in range(-50, 51, 5)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        cnvs.create_oval(cords[i], ZR, cords[i] + 2, ZR + 2, fill='black')
        cnvs.create_text(cords[i] + 5, ZR + 10, text=str(vals[i]))
        cnvs.create_oval(ZR, cords[i], ZR + 2, cords[i] + 2, fill='black')
        cnvs.create_text(ZR + 5, cords[i] + 10, text=str(-vals[i]))


def divide(lst_of_tp, i):
    new_lst = list()
    for each in lst_of_tp:
        new_tp = (each[0] / i, each[1] / i)
        new_lst.append(new_tp)
    return new_lst


def draw():
    cnvs.delete('all')
    n = int(amount.get())
    for i in range(1, n + 1):
        new_triangle = divide(MAIN_TR, i)
        new_triangle_scr = [dec_to_scr(i) for i in new_triangle]
        cnvs.create_polygon(new_triangle_scr, fill='white', outline='black')
    axis()


root = Tk()
root.title('Рисование')
root.geometry('500x600')
root.resizable(width=False, height=False)
cnvs = Canvas(root, width=WD, height=WD, bg='white')
cnvs.place(x=0, y=100)
scr_triangle = [dec_to_scr(i) for i in MAIN_TR]
cnvs.create_polygon(*scr_triangle, fill='white', outline='black')
axis()
Label(root, text='Количество\nтреугольников', width=20).grid(row=0, column=0)
amount = Entry(root, width=50)
amount.grid(row=0, column=1)
drawer = Button(root, text='Нарисовать', command=draw)
drawer.place(x=210, y=50)

root.mainloop()
