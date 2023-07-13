# Uloha 1

import turtle

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(2)
t.ht()


def ctverec(strana):
    t.pensize(5)
    for i in range(4):
        t.fd(strana)
        t.rt(90)


def trojuhelnik(strana):
    t.pensize(5)
    uhel = 120
    for i in range(3):
        t.fd(strana)
        t.lt(uhel)


def domek(strana, barva_strechy, barva_ctverce):
    t.pencolor(barva_ctverce)
    t.fillcolor(barva_ctverce)
    t.begin_fill()
    ctverec(strana)
    t.end_fill()
    t.pencolor(barva_strechy)
    t.fillcolor(barva_strechy)
    t.begin_fill()
    trojuhelnik(strana)
    t.end_fill()


domek(100, "red", "yellow")

turtle.exitonclick()
