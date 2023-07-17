import tkinter
import random

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def klavesa(event):
    char = event.char
    x = random.randint(100, 540)
    y = random.randint(100, 380)
    color = "#{:06x}".format(random.randrange(256 ** 3))
    font_size = "ariel {}".format(random.randint(7, 20))
    canvas.create_text(x, y, text=char, fill=color, font=font_size)


canvas.bind_all("<Key>", klavesa)

canvas.mainloop()
