from tkinter import *


def draw():
    cnvs.delete("all")
    cnvs.create_polygon(int(x1.get()), int(y1.get()), int(x2.get()), int(y2.get()),
                        int(x3.get()), int(y3.get()), fill='white', outline='black')


root = Tk()
root.title('Рисование треугольника')
root.geometry('400x540')
root.resizable(width=False, height=False)

cnvs = Canvas(root, width=400, height=400, bg='white')
cnvs.place(x=0, y=140)
x = Label(root, text='x', width=15)
x.grid(row=0, column=1)
y = Label(root, text='y', width=15)
y.grid(row=0, column=2)
top1 = Label(root, text='Вершина 1', width=15)
top1.grid(row=1, column=0)
x1 = Entry(root, width=20)
x1.grid(row=1, column=1)
y1 = Entry(root, width=20)
y1.grid(row=1, column=2)
top2 = Label(root, text='Вершина 2', width=15)
top2.grid(row=2, column=0)
x2 = Entry(root, width=20)
x2.grid(row=2, column=1)
y2 = Entry(root, width=20)
y2.grid(row=2, column=2)
top3 = Label(root, text='Вершина 3', width=15)
top3.grid(row=3, column=0)
x3 = Entry(root, width=20)
x3.grid(row=3, column=1)
y3 = Entry(root, width=20)
y3.grid(row=3, column=2)
drawer = Button(root, text='Нарисовать', command=draw)
drawer.place(x=50, y=100)
description = Label(root, text='Размер холста: 400×400', width=20)
description.place(x=215, y=105)

root.mainloop()
