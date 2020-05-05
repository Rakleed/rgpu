from tkinter import *

WD = 500
ZR = WD / 2
KF = 10


def dec_to_scr(cords):
    return round(cords[0] * KF + ZR), round(ZR - cords[1] * KF)


def axis():
    cnvs.create_line(0, 250, 500, 250, arrow=LAST, fill='green')
    cnvs.create_line(250, 500, 250, 0, arrow=LAST, fill='green')
    cnvs.create_text(WD - 20, ZR + 20, text='X')
    cnvs.create_text(ZR - 20, 20, text='Y', )
    vals = [i for i in range(-50, 50, 5)]
    cords = [int(ZR + i*KF) for i in vals]
    for i in range(len(cords)):
        cnvs.create_oval(cords[i], ZR, cords[i] + 2, ZR + 2, fill='green')
        cnvs.create_text(cords[i] + 5, ZR + 10, text=str(vals[i]), fill='green')
        cnvs.create_oval(ZR, cords[i], ZR + 2, cords[i] + 2, fill='green')
        cnvs.create_text(ZR + 5, cords[i] + 10, text=str(-vals[i]), fill='green')


def draw():
    # Антенна
    cnvs.create_oval(dec_to_scr((-1, 22)), dec_to_scr((1, 24)), fill='gray', outline='black')
    cnvs.create_polygon(dec_to_scr((-0.5, 22)), dec_to_scr((-1.1, 15)), dec_to_scr((1.1, 15)), dec_to_scr((0.5, 22)),
                        fill='gray', outline='black')
    # Фон головы
    cnvs.create_oval(dec_to_scr((-12.5, -5)), dec_to_scr((12.5, 15)), fill='gray', outline='gray')
    cnvs.create_polygon(dec_to_scr((-12.5, 5)), dec_to_scr((12.5, 5)), dec_to_scr((12.5, -20)),
                        dec_to_scr((-12.5, -20)), fill='gray', outline='gray')
    # Глаза, задний фон
    cnvs.create_oval(dec_to_scr((5.5, -5.5)), dec_to_scr((15.5, 5.5)), fill='gray', outline='gray')
    cnvs.create_oval(dec_to_scr((-15.5, -5.5)), dec_to_scr((-5.5, 5.5)), fill='gray', outline='gray')
    cnvs.create_polygon(dec_to_scr((-10.5, -5.5)), dec_to_scr((10.5, -5.5)), dec_to_scr((10.5, 5.5)),
                        dec_to_scr((-10.5, 5.5)), fill='gray', outline='gray')

    # Глаза
    cnvs.create_oval(dec_to_scr((5, -5)), dec_to_scr((15, 5)), fill='black', outline='black')
    cnvs.create_oval(dec_to_scr((-15, -5)), dec_to_scr((-5, 5)), fill='black', outline='black')
    cnvs.create_polygon(dec_to_scr((-10, -5)), dec_to_scr((10, -5)), dec_to_scr((10, 5)),
                        dec_to_scr((-10, 5)), fill='black', outline='black')
    # Глазные яблоки
    cnvs.create_oval(dec_to_scr((2, -4.5)), dec_to_scr((12, 4.5)), fill='#fff399')
    cnvs.create_oval(dec_to_scr((-12, -4.5)), dec_to_scr((-2, 4.5)), fill='#fff399')
    cnvs.create_rectangle(dec_to_scr((6.5, -0.5)), dec_to_scr((7.5, 0.5)), fill='black')
    cnvs.create_rectangle(dec_to_scr((-7.5, -0.5)), dec_to_scr((-6.5, 0.5)), fill='black')
    # Рот задний фон
    cnvs.create_oval(dec_to_scr((-12, -16)), dec_to_scr((-10, -9)), fill='black', outline='black')
    cnvs.create_oval(dec_to_scr((10, -16)), dec_to_scr((12, -9)), fill='black', outline='black')
    cnvs.create_rectangle(dec_to_scr((-11, -16)), dec_to_scr((11, -9)), fill='black', outline='black')
    # Рот
    cnvs.create_oval(dec_to_scr((-11.5, -15.5)), dec_to_scr((-10, -9.5)), fill='#fff399', outline='#fff399')
    cnvs.create_oval(dec_to_scr((10, -15.5)), dec_to_scr((11.5, -9.5)), fill='#fff399', outline='#fff399')
    cnvs.create_rectangle(dec_to_scr((-11, -15.5)), dec_to_scr((11, -9.5)), fill='#fff399', outline='#fff399')
    # "Зубы"
    cnvs.create_line(dec_to_scr((-11.75, -11.5)), dec_to_scr((11.75, -11.5)))
    cnvs.create_line(dec_to_scr((-11.75, -13.5)), dec_to_scr((11.75, -13.5)))
    cnvs.create_line(dec_to_scr((-11, -9)), dec_to_scr((-11, -16)))
    cnvs.create_line(dec_to_scr((-6.6, -9)), dec_to_scr((-6.6, -16)))
    cnvs.create_line(dec_to_scr((-2.2, -9)), dec_to_scr((-2.2, -16)))
    cnvs.create_line(dec_to_scr((2.2, -9)), dec_to_scr((2.2, -16)))
    cnvs.create_line(dec_to_scr((6.6, -9)), dec_to_scr((6.6, -16)))
    cnvs.create_line(dec_to_scr((11, -9)), dec_to_scr((11, -16)))


root = Tk()
root.title('Рисование')
root.geometry('500x500')
root.resizable(width=False, height=False)
cnvs = Canvas(root, width=WD, height=WD, bg='white')
cnvs.place(x=0, y=0)
draw()

root.mainloop()
