# Uloha 2
import random
import turtle

turtle.delay(10)
t = turtle.Turtle()
t.hideturtle()

def ctverec(strana):
    t.pensize(3)
    t.pencolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.fillcolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.begin_fill()
    for i in range(6):  # vcetne 2 cyklu presunu pro start trojuhelniku
        t.lt(90)
        t.fd(strana)
    t.end_fill()


def trojuhelnik(strana):
    t.pensize(3)
    t.pencolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.fillcolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.begin_fill()
    uhel = 120
    for i in range(3):
        t.rt(uhel)
        t.fd(strana)
    t.end_fill()
    t.pu()
    for i in range(2):
        t.lt(90)
        t.fd(strana)
    t.pd()


def domek(strana, posun):
    ctverec(strana)
    trojuhelnik(strana)
    t.pu()
    d = 15
    t.fd(posun + d)
    t.pd()

def ulice():
    street = []
    sirka_strany_domu = -1
    i = n = 0
    while sirka_strany_domu != 0:
        sirka_strany_domu = int(input("Zadej sirku strany kazdeho domku (ukoncis '0'): "))
        if sirka_strany_domu != 0:
            street.append(sirka_strany_domu)
    n = int(len(street))
    for i in range(n):
        if i < n - 1:
            domek(street[i], street[i + 1])
        elif i == n - 1:
            domek(street[i], street[i])


ulice()

turtle.exitonclick()
