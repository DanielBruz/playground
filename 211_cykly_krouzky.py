import tkinter
import random

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

for i in range(1000):
    x = random.randrange(640)
    y = random.randrange(480)
    canvas.create_oval(x,y,x+10, y+10)



canvas.mainloop()