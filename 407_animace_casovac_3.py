import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def tik():
    global smer
    x1, y1, _, _ = canvas.coords(oval_id)   # vrati pozici objektu s urcitym ID
    if x1 <= 0:
        smer = 1
    elif x1 + 40 >= 640:
        smer = -1
    canvas.move(oval_id, smer * 5, 0)
    canvas.after(20, tik)


oval_id = canvas.create_oval(100, 100, 140, 140, width=2)
smer = 1
tik()

canvas.mainloop()
