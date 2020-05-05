from tkinter import *


WD = 500
HG = 500
ZR = 250
KF = 10


def func(x):
    a = int(a_const.get())
    b = int(b_const.get())
    c = int(a_const.get())
    return a*x*x + b*x + c


def axis_description():
    canv.create_text(WD-15, ZR+20, text='X')
    canv.create_text(ZR-20, 20, text='Y', )
    vals = [i for i in range(-50, 51, 5)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        canv.create_oval(cords[i], ZR, cords[i]+2, ZR+2, fill='black')
        canv.create_text(cords[i]+5, ZR+10, text=str(vals[i]))
        canv.create_oval(ZR, cords[i], ZR+2, cords[i]+2, fill='black')
        canv.create_text(ZR+5, cords[i]+10, text=str(-vals[i]))



def draw():
    canv.delete("all")
    canv.create_line(0, 250, 500, 250, arrow=LAST)
    canv.create_line(250, 500, 250, 0, arrow=LAST)
    axis_description()
    x_mn = int(x_min.get())
    x_mx = int(x_max.get())
    y_mn = int(y_min.get())
    y_mx = int(y_max.get())
    x = x_mn
    while x <= x_mx:
        xc = round(ZR + x*KF)
        yc = round(ZR - func(x)*KF)
        if ZR - y_mn*KF >= yc >= ZR - y_mx*KF:
            canv.create_oval(xc, yc, xc+1, yc+1)
        x += 1/100


root = Tk()
root.title('График функции')
root.geometry('500x650')
root.resizable(width=False, height=False)
canv = Canvas(root, width=WD, height=HG, bg='white')
canv.place(x=0, y=150)
canv.create_line(0, 250, 500, 250, arrow=LAST)
canv.create_line(250, 500, 250, 0, arrow=LAST)
axis_description()
a_label = Label(root, text='a', width=5)
a_label.grid(row=0, column=0)
b_label = Label(root, text='b', width=5)
b_label.grid(row=1, column=0)
c_label = Label(root, text='с', width=5)
c_label.grid(row=2, column=0)
a_const = Entry(root, width=12)
a_const.grid(row=0, column=1)
b_const = Entry(root, width=12)
b_const.grid(row=1, column=1)
c_const = Entry(root, width=12)
c_const.grid(row=2, column=1)
space = Label(root, text='', width=7)
space.grid(row=0, column=2)
space = Label(root, text='', width=7)
space.grid(row=1, column=2)
x_min_label = Label(root, text='x min', width=5)
x_min_label.grid(row=0, column=3)
x_min = Entry(root, width=12)
x_min.grid(row=0, column=4)
y_min_label = Label(root, text='y min', width=5)
y_min_label.grid(row=0, column=6)
y_min = Entry(root, width=12)
y_min.grid(row=0, column=7)
x_max_label = Label(root, text='x max', width=5)
x_max_label.grid(row=1, column=3)
x_max = Entry(root, width=12)
x_max.grid(row=1, column=4)
y_max_label = Label(root, text='y max', width=5)
y_max_label.grid(row=1, column=6)
y_max = Entry(root, width=12)
y_max.grid(row=1, column=7)
space = Label(root, text='', width=7)
space.grid(row=0, column=5)
space = Label(root, text='', width=7)
space.grid(row=1, column=5)
drawer = Button(root, text='Нарисовать', command=draw)
drawer.place(x=70, y=95)
description = Label(root, text='Размер вводите в декартовых координатах.')
description.place(x=200, y=95)

root.mainloop()
