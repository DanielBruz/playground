import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()
rect_id = None


def klavesa(event):
    print(repr(event))


canvas.bind_all("<Key>", klavesa)
canvas.mainloop()
