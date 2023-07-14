# Uloha 2
import turtle
import random

turtle.delay(10)
t = turtle.Turtle()
t.hideturtle()

def ctverec(strana):
    t.pensize(3)
    t.pencolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.fillcolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.begin_fill()
    for i in range(4):
        t.lt(90)
        t.fd(strana)
    t.end_fill()
    t.pu()
    t.lt(90)
    t.fd(strana)
    t.pd()

def trojuhelnik(strana):
    t.pensize(3)
    t.pencolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.fillcolor("#{:06x}".format(random.randrange(256 ** 3)))
    t.pu()
    t.lt(90)
    t.fd(strana)
    t.pd()
    t.begin_fill()
    uhel = 120
    for i in range(3):
        t.rt(uhel)
        t.fd(strana)
    t.end_fill()

def startovaci_pozice(strana, posun):
    t.pu()
    for i in range(2):
        t.lt(90)
        t.fd(strana)
    t.fd(posun)
    t.pd()

def domek(strana, posun):
    ctverec(strana)
    trojuhelnik(strana)
    startovaci_pozice(strana, posun)

def ulice():
    street = []
    sirka_strany_domu = -1
    i = 0
    j = 0
    n = 0
    posun = 0
    while sirka_strany_domu != 0:
        sirka_strany_domu = int(input("Zadej sirku strany kazdeho domku (ukoncis '0'): "))
        if sirka_strany_domu != 0:
            street.append(sirka_strany_domu)
    n = int(len(street))
    for j in range(n):
        if street[j] > street[j-1]:
            posun = street[j] + abs(street[j] - street[j-1])
        else:
            posun = street[j-1] + abs(street[j] - street[j-1])
        domek(street[j], posun)

ulice()

turtle.exitonclick()


