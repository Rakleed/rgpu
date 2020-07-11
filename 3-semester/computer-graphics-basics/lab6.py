from tkinter import *
import math

WD = 500
ZR = WD / 2
KF = 10
FLAG = [(5, 5), (5, 16), (10, 16), (7, 13), (10, 10), (6, 10), (6, 5)]


def dec_to_scr(cords: tuple):
    return cords[0] * KF + ZR, ZR - cords[1] * KF


def axis():
    cnvs.delete("all")
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


def transl_to_rad(x):
    return x * math.pi / 180


def transfer():
    axis()
    if int(angle.get()) == 0:
        matrix = ((float(a11.get()), float(a12.get())),
                  (float(a21.get()), float(a22.get())))
    else:
        matrix = ((math.cos(transl_to_rad(int(angle.get()))), math.sin(transl_to_rad(int(angle.get())))),
                  (-math.sin(transl_to_rad(int(angle.get()))), math.cos(transl_to_rad(int(angle.get())))))
    new_flag = list()
    for each in FLAG:
        new_cords = (each[0]*matrix[0][0] + each[1]*matrix[1][0],
                     each[0]*matrix[0][1] + each[1]*matrix[1][1])
        new_flag.append(new_cords)
    new_flag_scr = [dec_to_scr(i) for i in new_flag]
    cnvs.create_polygon(new_flag_scr)


root = Tk()
root.title('Рисование')
root.geometry('500x580')
root.resizable(width=False, height=False)
cnvs = Canvas(root, width=WD, height=WD, bg='white')
cnvs.place(x=0, y=80)
axis()
FLAG_scr = [dec_to_scr(i) for i in FLAG]
cnvs.create_polygon(*FLAG_scr)
transfer_label = Label(root, text='Матрица преобразования', width=25)
transfer_label.grid(row=0, column=0)
a11 = Entry(root, width=5)
a11.grid(row=0, column=1)
a12 = Entry(root, width=5)
a12.grid(row=0, column=2)
a21 = Entry(root, width=5)
a21.grid(row=1, column=1)
a22 = Entry(root, width=5)
a22.grid(row=1, column=2)
angle_label = Label(root, text='Угол поворота\n(если не указан — 0)', width=25)
angle_label.grid(row=3, column=0)
angle = Entry(root, width=5)
angle.grid(row=3, column=1)
transfer_button = Button(text='Преобразовать', command=transfer)
transfer_button.place(x=350, y=27)

root.mainloop()
