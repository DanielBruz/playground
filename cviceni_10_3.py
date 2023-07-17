import tkinter
import random

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def mouse_drag(event):
    global rect_id
    global souradnice
    canvas.delete(rect_id)
    rect_id = canvas.create_rectangle(souradnice, fill="red")
    canvas.move(rect_id, event.x-75, event.y-125)


souradnice = 50, 100, 100, 150
rect_id = canvas.create_rectangle(souradnice, fill="red")
canvas.bind("<B1-Motion>", mouse_drag)

canvas.mainloop()
