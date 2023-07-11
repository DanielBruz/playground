import tkinter
import random

width=640
height=480
canvas = tkinter.Canvas(width=width, height=height, bg="grey")
canvas.pack()

def vzdalenost(x1, y1, x2, y2):
    return (((x2-x1)**2)+((y2-y1)**2))**.5

def barva(vzd):
    normalize = 255 - int((vzd/400)*255)
    color = "#{0:02x}{0:02x}{0:02x}".format(normalize)
    return color

def kresli_ctverec(x, y, velikost, barva):
    souradnice = (x - velikost / 6, y - velikost / 6, x + velikost / 6, y + velikost / 6)
    canvas.create_rectangle(souradnice, fill=barva, outline="blue", width=2)
def kresli_ctverce(pocet):
    for x in range(pocet):
        x = random.randrange(width)
        y = random.randrange(height)
        vzd = vzdalenost(x,y,width/2,height/2)
        color = barva(vzd)
        kresli_ctverec(x,y, vzd/6, color)

kresli_ctverce(1000)

canvas.mainloop()

