import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def create_oval(event):
    oval_id = canvas.create_oval(event.x - 20, event.y - 20,
                                 event.x + 20, event.y + 20)


canvas.bind("<ButtonPress-1>", create_oval)
canvas.mainloop()
