import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


def spracuj_udalost(event):
    print(repr(event))


def motion(event):
    print("hybem sa na {},{}".format(event.x, event.y))


def drag(event):
    print("ťahám myšku na {},{}".format(event.x, event.y))


def press(event):
    print("stlačil som na {},{}".format(event.x, event.y))


def release(event):
    print("pustil som na {},{}".format(event.x, event.y))


canvas.bind("<Button-1>", spracuj_udalost)
canvas.bind("<Motion>", motion)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonPress-1>", press)
canvas.bind("<ButtonRelease-1>", release)

canvas.mainloop()
