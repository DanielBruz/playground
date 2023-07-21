import tkinter
import random
class Stvorec:
    canvas = None  # nechcem používať globálnu premennú canvas ako sme to
                   # doteraz robili. globálne premenné je zlý programovací
                   # štýl.
    def __init__(self, x, y, velkost=40):
        self.velkost = velkost
        self.id = self.canvas.create_rectangle(x-velkost/2, y-velkost/2,
                                                x+velkost/2, y+velkost/2,
                                                fill="gray")
    def nahodny_pohyb(self):
        dx = random.randrange(-5, 5)
        dy = random.randrange(-5, 5)
        self.canvas.move(self.id, dx, dy)
def tik():
    for s in stvorce:
        s.nahodny_pohyb()
    Stvorec.canvas.after(10, tik)


Stvorec.canvas = tkinter.Canvas(width=640, height=480)
Stvorec.canvas.pack()

stvorce = [Stvorec(random.randrange(640), random.randrange(480)) for i in range(100)]

tik()

Stvorec.canvas.mainloop()
