from tkinter import *
import math

WD = 500
HG = 250
ZR_X = 10
ZR_Y = 240
g = 9.8


def draw_axis():
    cnvs.create_text(WD - 20, ZR_Y - 20, text='X')
    cnvs.create_text(ZR_X + 20, 20, text='Y')
    x_vals = [i/10 for i in range(21)]
    y_vals = [i/10 for i in range(11)]
    x_cords = [ZR_X+x_vals[i]*240 for i in range(len(x_vals))]
    y_cords = [ZR_Y-y_vals[i]*230 for i in range(len(y_vals))]
    for i in range(len(x_cords)):
        cnvs.create_oval(x_cords[i], ZR_Y, x_cords[i] + 2, ZR_Y + 2, fill='black')
    for j in range(len(y_cords)):
        cnvs.create_oval(ZR_X, y_cords[j], ZR_X + 2, y_cords[j] + 2, fill='black')


def x_func(t):
    v = int(v0.get())
    ang = int(angle.get()) * math.pi/180
    return v * t * math.cos(ang)


def y_func(t):
    v = int(v0.get())
    ang = int(angle.get()) * math.pi/180
    return v * t * math.sin(ang) - g * t * t / 2


def draw():
    cnvs.delete("all")
    cnvs.create_line(0, 240, 490, 240, arrow=LAST)
    cnvs.create_line(10, 250, 10, 10, arrow=LAST)
    draw_axis()
    tm = float(time.get())
    i = 0
    xc = 0
    yc = 0
    while i <= tm:
        xc = round(ZR_X + x_func(i)*100)
        yc = round(ZR_Y - y_func(i)*100)
        if yc <= 240:
            cnvs.create_oval(xc, yc, xc + 1, yc + 1)
        i += tm/1000
    print(xc)
    print(yc)


root = Tk()
root.title('График функции')
root.geometry('500x380')
root.resizable(width=False, height=False)
cnvs = Canvas(root, width=WD, height=HG, bg='white')
cnvs.place(x=0, y=130)
v0_label = Label(root, text='Начальная скорость', width=20)
v0_label.grid(row=0, column=0)
v0 = Entry(root, width=30)
v0.grid(row=0, column=1)
angle_label = Label(root, text='Угол', width=20)
angle_label.grid(row=1, column=0)
angle = Entry(root, width=30)
angle.grid(row=1, column=1)
time_label = Label(root, text='Время', width=20)
time_label.grid(row=2, column=0)
time = Entry(root, width=30)
time.grid(row=2, column=1)
drawer = Button(root, text='Нарисовать', command=draw)
drawer.place(x=200, y=90)

root.mainloop()
