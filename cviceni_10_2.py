import tkinter
import random

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def zmen_barvu(event):
    color = "#{:06x}".format(random.randrange(256 ** 3))
    if (event.y >= 100) and (event.y <= 150):
        if (event.x >= strana) and (event.x <= 2 * strana):
            canvas.itemconfig(a[0], fill=color)
        elif (event.x >= 2 * strana + posun) and (event.x <= 3 * strana + posun):
            canvas.itemconfig(a[1], fill=color)
        elif (event.x >= 3 * strana + 2 * posun) and (event.x <= 4 * strana + 2 * posun):
            canvas.itemconfig(a[2], fill=color)
        elif (event.x >= 4 * strana + 3 * posun) and (event.x <= 5 * strana + 3 * posun):
            canvas.itemconfig(a[3], fill=color)
        elif (event.x >= 5 * strana + 4 * posun) and (event.x <= 6 * strana + 4 * posun):
            canvas.itemconfig(a[4], fill=color)
        elif (event.x >= 6 * strana + 5 * posun) and (event.x <= 7 * strana + 5 * posun):
            canvas.itemconfig(a[5], fill=color)
        elif (event.x >= 7 * strana + 6 * posun) and (event.x <= 8 * strana + 6 * posun):
            canvas.itemconfig(a[6], fill=color)
        elif (event.x >= 8 * strana + 7 * posun) and (event.x <= 9 * strana + 7 * posun):
            canvas.itemconfig(a[7], fill=color)


def navrat(event):
    i = 0
    while i < n:
        canvas.itemconfig(a[i], fill="black")
        i += 1


n = 8
a = []
strana = 50
x1 = 50
y1 = 100
x2 = x1 + strana
y2 = y1 + strana
posun = 20

for i in range(n):
    rect_id = canvas.create_rectangle(x1, y1, x2, y2, width=3, fill="black")
    x1 += (strana + posun)
    x2 += (strana + posun)
    a.append(rect_id)

canvas.bind("<ButtonPress-1>", zmen_barvu)
canvas.bind("<ButtonRelease-1>", navrat)

canvas.mainloop()
