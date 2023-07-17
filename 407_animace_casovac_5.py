import tkinter
import random
import math

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


# zkombinujeme s udalostmi. Na pohyb nepouzijeme funkci MOVE, budeme objektu menit souradnice.

def tik():
    global uhel
    uhel = (uhel + 5) % 360
    x = cx + math.cos(math.radians(uhel)) * 40
    y = cy + math.sin(math.radians(uhel)) * 40
    canvas.coords(oval_id, x - 20, y - 20, x + 20, y + 20)  # prekresli objekt na nove souradnice
    canvas.after(20, tik)


def tok():
    color = "#{:06x}".format(random.randrange(256 ** 3))
    canvas.itemconfig(oval_id, fill=color)
    canvas.after(500, tok)


def mouse_move(event):
    global cx, cy
    cx = event.x
    cy = event.y


canvas.bind("<Motion>", mouse_move)
cx = 320
cy = 240
oval_id = canvas.create_oval(cx - 20, cy - 20, cx + 20, cy + 20)
uhel = 0
tik()
tok()

canvas.mainloop()
