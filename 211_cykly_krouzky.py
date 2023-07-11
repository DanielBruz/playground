import tkinter
import random

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

for i in range(1000):
    x = random.randrange(640)
    y = random.randrange(480)
    if x > 320 and y > 240:
        canvas.create_oval(x,y,x+10, y+10, fill = "red")
    elif x > 320 and y < 240:
        canvas.create_oval(x, y, x + 10, y + 10, fill="blue")
    elif x < 320 and y > 240:
        canvas.create_oval(x, y, x + 10, y + 10, fill ="yellow")
    else:
        canvas.create_oval(x, y, x + 10, y + 10, fill="purple")

canvas.mainloop()