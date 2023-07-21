import turtle
import random


class Stvorcova(turtle.Turtle):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.speed(0)
        self.pu()
        self.setpos(x, y)
        self.pd()

    def stvorec(self, velkost):
        for i in range(4):
            self.fd(velkost)
            self.rt(90)


class Vlnovkova(Stvorcova):
    def fd(self, dlzka):
        while dlzka >= 5:
            self.lt(60)
            super().fd(5)
            self.rt(120)
            super().fd(5)
            self.lt(60)
            dlzka -= 5
        super().fd(dlzka)


class Kriva(Stvorcova):
    def fd(self, dlzka):
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)
        self.rt(180 - random.randint(-3, 3))
        super().fd(dlzka)


turtle.tracer(0)
korytnacky = []
for x in range(-350, 350, 50):
    for y in range(-350, 350, 50):
        k = Kriva(x, y)
        k.ht()
        korytnacky.append(k)

for k in korytnacky:
    k.stvorec(50)
    turtle.update()

turtle.mainloop()
