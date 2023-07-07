import tkinter
import random
canvas = tkinter.Canvas(width=640, height=480, bg="gray")
canvas.pack()

def vzdialenost(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5

def farba(vzd):
    normalize = 255 - int((vzd/400)*255)
#   print(vzd,normalize)
    return "#{0:02x}{0:02x}{0:02x}".format(normalize)

def kresli_stvorec(x, y, velkost, farba):
    suradnice = (x-velkost/2, y-velkost/2, x+velkost/2, y+velkost/2)
    canvas.create_rectangle(suradnice, fill=farba)

def kresli_stvorce(pocet):
    for x in range(pocet):
        x = random.randrange(640)
        y = random.randrange(480)
        vzd = vzdialenost(x,y,320,240)
        color = farba(vzd)
        kresli_stvorec(x,y, vzd/6, color)

kresli_stvorce(1000)

canvas.mainloop()