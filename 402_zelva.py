import turtle
import random
import time

# Uloha 1

#turtle.delay(0)
#t = turtle.Turtle()
#t.speed(10)

#for i in range(10000):
#    t.seth(random.randrange(360))
#    t.fd(10)

# Uloha 2

#def ctverec(tu, delka):
#    for i in range(4):
#        tu.fd(delka)
#        tu.rt(90)
#def posun(tu):
#    tu.pu()
#    tu.setpos(random.randint(-300,300),
#             random.randint(-300, 300))
#    tu.seth(random.randrange(360))
#    tu.pd()

#t1 = turtle.Turtle()
#t2 = turtle.Turtle()

#posun(t1)
#posun(t2)

#ctverec(t1, 100)
#ctverec(t2, 50)

# Uloha 3

#turtle.tracer(0)
#def ctverec(tu, delka):
#    for i in range(4):
#        tu.fd(delka)
#        tu.rt(90)
#def posun(tu):
#    tu.pu()
#    tu.setpos(random.randint(-300,300),
#             random.randint(-300, 300))
#    tu.seth(random.randrange(360))
#    tu.pd()

#turtles = [turtle.Turtle() for x in range(100)]
#for t in turtles:
#    posun(t)
#    ctverec(t, 40)
#    turtle.update()

# Uloha 4

#turtle.tracer(0)
#turtles = []
#for i in range(60):
#    turtles.append(turtle.Turtle())
#    turtles[-1].seth(i * 6)

#for x in range(360):
#    for t in turtles:
#        t.fd(5)
#        t.rt(3) # random.randint(1, 15)
#    turtle.update()
#time.sleep(2)

# Uloha 5

n = 10 # pocet zelvicek
turtles = []    # prazdne pole zelvicek
turtle.tracer(0)    # 0 = mam vykreslovani manualne pod kontrolou
turtle.bgcolor("black")
for i in range(n):
    t = turtle.Turtle()
    t.pensize(1)
    t.pencolor("#{:06x}".format(random.randrange(256**3)))  # 3 kanaly RGB po 256
    t.pu()
    t.setpos(random.randint(-300, 300),
             random.randint(-300, 300))
    t.ht()  # skryjeme logo zelvy - hide turtle
    t.pd()
    turtles.append(t)   # doplnim naformatovanou zelvu do pole
while True:
    for i in range(n):  # pro vsechnz moje zelvy
        j = (i + 1) % n # index nasledujici zelvy pomoci zbytku po deleni
        uhel = turtles[i].towards(turtles[j])   # o jaky uhel se mam otocit s zevlou "i", abych smeroval k zelve "j"
        vzd = turtles[i].distance(turtles[j])   # vzdalenost obou zelvicek
        turtles[i].seth(uhel)
        turtles[i].fd(vzd)  # nakreslim celou caru smerem k druhe zelve
        turtles[i].fd(vzd/10 - vzd)  # zaporne cislo; vracim se o kousek zpet
    turtle.update()
