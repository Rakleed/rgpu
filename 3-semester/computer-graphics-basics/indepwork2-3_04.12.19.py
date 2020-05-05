from tkinter import *
import math

WD = 500
ZR = WD / 2
KF = 25
DIAM = 10
RAD = DIAM/2
LENGTH = 3


def dec_to_scr(cords):
    return round(cords[0] * KF + ZR), round(ZR - cords[1] * KF)


def atrd(x):
    return x * math.pi / 180


def axis():
    cnvs.create_line(0, 250, 500, 250, arrow=LAST)
    cnvs.create_line(250, 500, 250, 0, arrow=LAST)
    cnvs.create_text(WD - 20, ZR + 20, text='X')
    cnvs.create_text(ZR - 20, 20, text='Y', )
    vals = [i for i in range(-10, 10)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        cnvs.create_oval(cords[i], ZR, cords[i] + 2, ZR + 2, fill='black')
        cnvs.create_text(cords[i] + 5, ZR + 10, text=str(vals[i]))
        cnvs.create_oval(ZR, cords[i], ZR + 2, cords[i] + 2, fill='black')
        cnvs.create_text(ZR + 5, cords[i] + 10, text=str(-vals[i]))


def draw():
        cnvs.delete('all')
        x = int(x_dec.get())
        y = -int(y_dec.get())
        angle = 0
        x0 = RAD * math.cos(angle) + x
        y0 = RAD * math.sin(angle) - y
        p1 = (x0, y0)
        for i in range(31):
            ang = angle + 2 * math.pi * i / 30
            xi = RAD * math.cos(ang) + x
            yi = RAD * math.sin(ang) - y
            p2 = (xi, yi)
            print(p1, p2)
            cnvs.create_line(dec_to_scr(p1), dec_to_scr(p2), arrow=LAST)
            p1 = p2
        axis()


root = Tk()
root.title('Рисование')
root.geometry('500x600')
root.resizable(width=False, height=False)
cnvs = Canvas(root, width=WD, height=WD, bg='white')
cnvs.place(x=0, y=100)
axis()
Label(root, text='', width=19).grid(row=0, column=0)
Label(root, text='x', width=15).grid(row=0, column=1)
Label(root, text='y', width=15).grid(row=0, column=2)
x_dec = Entry(root, width=15)
x_dec.grid(row=1, column=1)
y_dec = Entry(root, width=15)
y_dec.grid(row=1, column=2)
drawer = Button(root, text='Нарисовать', command=draw)
drawer.place(x=210, y=50)

root.mainloop()
