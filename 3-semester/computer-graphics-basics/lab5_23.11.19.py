from tkinter import *
import math


WD = 500
ZR = 250
PHI = 0
RADIUS = 200


def translation_to_radians(x):
    return x * math.pi / 180


def draw():
    cnvs.delete('all')
    n = int(angl.get())
    ang = translation_to_radians(PHI)
    x0 = round(RADIUS * math.cos(ang))
    y0 = round(RADIUS * math.sin(ang))
    p1 = (x0 + ZR, ZR - y0)
    for i in range(n + 1):
        ang = PHI + 2 * math.pi * i / n
        xi = round(RADIUS * math.cos(ang))
        yi = round(RADIUS * math.sin(ang))
        p2 = (xi + ZR, ZR - yi)
        print(p1, p2)
        cnvs.create_line(p1, p2)
        p1 = p2


root = Tk()
root.title('Рисование')
root.geometry('500x560')
root.resizable(width=False, height=False)
cnvs = Canvas(root, width=WD, height=WD, bg='white')
cnvs.place(x=0, y=60)
angl_label = Label(root, text='Количество углов', width=30)
angl_label.grid(row=0, column=0)
angl = Entry(root, width=30)
angl.grid(row=0, column=1)
drawer = Button(root, text='Нарисовать', command=draw)
drawer.place(x=200, y=30)

root.mainloop()
