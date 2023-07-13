import turtle
import random
import time

# Uloha 1

#def ctverec(delka):
#    for i in range(4):
#        t.fd(delka)
#        t.rt(90)

#t = turtle.Turtle()
#ctverec(100)
#t.pu()
#t.lt(70)
#t.fd(80)
#t.pd()
#ctverec(50)

# Uloha 2

#def ctverec(delka):
#    for i in range(4):
#        t.fd(delka)
#        t.rt(90)
#def posun():
#    t.pu()
#    t.setpos(random.randint(-300,300),
#             random.randint(-300, 300))
#    t.seth(random.randrange(360))
#    t.pd()

#t = turtle.Turtle()
#t.speed(10)

#for i in range(10):
#    posun()
#    t.pensize(5)
#    if random.randrange(2):
#        t.fillcolor("red")
#        t.pencolor("red")
#    else:
#        t.fillcolor("blue")
#        t.pencolor("blue")
#    if random.randrange(2):
#        t.begin_fill()
#        t.end_fill()
#    ctverec(40)

# Uloha 3

#turtle.delay(0)
#t = turtle.Turtle()
#t.speed(10)
#while True:
#    uhel = random.randint(30, 70)
#    print("Spirala s uhlem: ", uhel)
#    for i in range(3, 300, 1):
#        t.fd(i)
#        t.rt(uhel)
#    time.sleep(2)
#    t.reset()
#    t.speed(10)

# Uloha 4

turtle.tracer(2,0)
turtle.bgcolor("black")
t = turtle.Turtle()
t.shape("turtle")
t.pencolor("yellow")
for uhel in range(2000):
    t.fd(8)
    t.rt(uhel+0.1)
time.sleep(2)
