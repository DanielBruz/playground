import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def press(event):
    canvas.create_text(event.x, event.y, text="({},{})".format(event.x, event.y), font="ariel 7")


canvas.bind("<ButtonPress-1>", press)

canvas.mainloop()
