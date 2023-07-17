import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()


# v tomto pripade vola casovac sam sebe
def tik():
    print("tik")
    canvas.after(500, tik)  # timer - casovac


tik()

canvas.mainloop()
