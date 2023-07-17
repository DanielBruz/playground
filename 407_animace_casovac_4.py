import tkinter
import random

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def tik():
    global smer
    x1, y1, _, _ = canvas.coords(oval_id)
    if x1 <= 0:
        smer = 1
    elif x1 + 40 >= 640:
        smer = -1
    canvas.move(oval_id, smer * 5, 0)
    canvas.after(20, tik)


def tok():
    color = "#{:06x}".format(random.randrange(256 ** 3))
    canvas.itemconfig(oval_id, fill=color)
    canvas.after(500, tok)


oval_id = canvas.create_oval(100, 100, 140, 140)
smer = 1

tik()
tok()

canvas.mainloop()
