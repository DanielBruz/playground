import turtle
import random
n = 10
turtles = []
turtle.tracer(0)
turtle.bgcolor("black")
for i in range(n):
    t = turtle.Turtle()
    t.pensize(1)
    t.pencolor("#{:06x}".format(random.randrange(256**3)))
    t.pu()
    t.setpos(random.randint(-300, 300),
             random.randint(-300, 300))
    t.pd()
    t.ht()
    turtles.append(t)
while True:
    for i in range(n):
        j = (i + 1) % n  # index nasledujici
        uhel = turtles[i].towards(turtles[j])
        vzd = turtles[i].distance(turtles[j])
        turtles[i].seth(uhel)
        turtles[i].fd(vzd)
        turtles[i].fd(vzd/10 - vzd)
    turtle.update()
