from tkinter import *
import math

WD = 500
ZR = WD / 2
KF = 10
TRIANG = [(-5, 5), (0, 15), (5, 5)]
DIAM = 10
RAD = DIAM/2


def dec_to_scr(cords: tuple):
    return round(cords[0] * KF + ZR), round(ZR - cords[1] * KF)


def axis():
    cnvs.create_line(0, 250, 500, 250, arrow=LAST)
    cnvs.create_line(250, 500, 250, 0, arrow=LAST)
    cnvs.create_line(0, 500, 500, 0, arrow=LAST)
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


def turner(lst_of_tp, ang):
    new_lst = list()
    for each in lst_of_tp:
        new_tp = (each[0]*math.cos(ang), each[1]*math.sin(ang))
        new_lst.append(new_tp)
    return new_lst


def draw1():
    cnvs.delete('all')
    angle = transl_to_rad(int(angle1.get()))
    matrix = ((math.cos(angle), math.sin(angle)),
              (-math.sin(angle), math.cos(angle)))

    new_triangle = list()
    for each in TRIANG:
        new_cords = (each[0]*matrix[0][0] + each[1]*matrix[1][0],
                     each[0]*matrix[0][1] + each[1]*matrix[1][1])
        new_triangle.append(new_cords)
    new_triangle_scr = [dec_to_scr(i) for i in new_triangle]
    cnvs.create_polygon(*new_triangle_scr, fill='white', outline='black')
    axis()


def draw2():
    cnvs.delete('all')
    angle = transl_to_rad(int(angle2.get()))
    angle45 = transl_to_rad(45)
    matrix = ((math.cos(angle), math.sin(angle)),
              (-math.sin(angle), math.cos(angle)))
    matrix45 = ((math.cos(angle45), math.sin(angle45)),
               (-math.sin(angle45), math.cos(angle45)))
    new_triangle1 = list()
    for each in TRIANG:
        new_cords1 = (each[0]*matrix[0][0] + each[1]*matrix[1][0],
                     each[0]*matrix[0][1] + each[1]*matrix[1][1])
        new_triangle1.append(new_cords1)
    new_triangle45 = list()
    for each in new_triangle1:
        new_cords45 = (each[0] * matrix45[0][0] + each[1] * matrix45[1][0],
                       each[0] * matrix45[0][1] + each[1] * matrix45[1][1])
        new_triangle45.append(new_cords45)
    new_triangle45_scr = [dec_to_scr(i) for i in new_triangle45]
    cnvs.create_polygon(*new_triangle45_scr, fill='white', outline='black')
    axis()


root = Tk()
root.title('Рисование')
root.geometry('500x580')
root.resizable(width=False, height=False)
cnvs = Canvas(root, width=WD, height=WD, bg='white')
cnvs.place(x=0, y=80)
axis()
TRIANG_scr = [dec_to_scr(i) for i in TRIANG]
cnvs.create_polygon(*TRIANG_scr, fill='white', outline='black')
angle1_label = Label(root, text='Угол поворота\nпо оси y = 0', width=20)
angle1_label.grid(row=0, column=0)
angle1 = Entry(root, width=10)
angle1.grid(row=0, column=1)
angle2_label = Label(root, text='Угол поворота\nпо оси y = x', width=20)
angle2_label.grid(row=1, column=0)
angle2 = Entry(root, width=10)
angle2.grid(row=1, column=1)

transfer_button1 = Button(text='Повернуть по y = 0', command=draw1)
transfer_button1.place(x=300, y=5)
transfer_button2 = Button(text='Повернуть по y = 0', command=draw2)
transfer_button2.place(x=300, y=45)

root.mainloop()
