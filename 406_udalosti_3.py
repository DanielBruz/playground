import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()
rect_id = None


def mouse_drag(event):
    x1, y1, x2, y2 = canvas.coords(rect_id)
    canvas.coords(rect_id, x1, y1, event.x, event.y)


def create_rect(event):
    global rect_id
    rect_id = canvas.create_rectangle(event.x, event.y, event.x, event.y)


canvas.bind("<B1-Motion>", mouse_drag)
canvas.bind("<ButtonPress-1>", create_rect)

canvas.mainloop()
