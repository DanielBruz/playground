import turtle
import time
import random

# priklad 1

#t = turtle.Turtle()
#def strom(n):
#    if n == 0:
#        t.fd(30)     # triviálni prípad
#        t.bk(30)
#    else:
#        t.fd(30)
#        t.lt(40)     # natoc se na kresleni leveho podstromu
#        strom(n - 1) # nakresli levy podstrom (n-1). urovne
#        t.rt(80)     # natoc se na kresleni pravého podstromu
#        strom(n - 1) # nakresli pravý podstrom (n-1). urovne
#        t.lt(40)     # natoc sa do puvodniho smeru
#        t.bk(30)     # vrat se na puvodni misto
#t.lt(90)
#strom(4)
#time.sleep(2)

# priklad 2 - menime parametry v zavislosti na hloubce rekurze

#def strom(n, d):
#    t.fd(d)
#    if n > 0:
#        t.lt(40)
#        strom(n - 1, d * .7)
#        t.rt(75)
#        strom(n - 1, d * .6)
#        t.lt(35)
#    t.bk(d)
#t = turtle.Turtle()
#t.lt(90)
#strom(5, 80)
#time.sleep(2)

# priklad 3 - nakreslime les

#def strom(n, d):
#    t.pensize(2 * n + 1)
#    t.fd(d)
#    if n == 0:
#        t.dot(10, 'green')
#    else:
#        uhol1 = random.randint(20, 40)
#        uhol2 = random.randint(20, 60)
#        t.lt(uhol1)
#        strom(n - 1, d * random.randint(40, 70) / 100)
#        t.rt(uhol1 + uhol2)
#        strom(n - 1, d * random.randint(40, 70) / 100)
#        t.lt(uhol2)
#    t.bk(d)
#turtle.tracer(20,0)
#t = turtle.Turtle()
#t.pencolor('maroon')
#t.lt(90)
#for i in range(30):
#    x = random.randint(-300, 300)
#    y = random.randint(-300, 100)
#    t.pu()
#    t.setpos(x,y)
#    t.pd()
#    strom(random.randint(3,7), random.randint(50,180))
#time.sleep(2)

# priklad 4 - Sierpiňského trojuhelník
#def trojuhelniky(n, a):
#    if n > 0:
#        for i in range(3):
#            t.fd(a)
#            t.rt(120)
#            trojuhelniky(n - 1, a / 2)
#turtle.tracer(10,0)
#t = turtle.Turtle()
#t.rt(60)
#trojuhelniky(6, 400)
#time.sleep(3)

# priklad 5 - Kochova (snehova) vlocka (krivka)

#turtle.tracer(0,0)
#t = turtle.Turtle()
#def koch(n, d):    # vykresli jen jednu stranu
#    if n == 1:
#        t.fd(d)
#    else:
#        koch(n-1, d/3)
#        t.lt(45)
#        koch(n-1,d/3)
#        t.rt(90)
#        koch(n-1, d/3)
#        t.lt(45)
#        koch(n-1,d/3)
#for i in range(4): # cyklus nam vykresli vsechny 4 strany
#    koch(4,100)
#    t.rt(360/4)
#    turtle.update()
#turtle.exitonclick()    # ukonceni na kliknuti

# priklad 6 - Koch 2

#turtle.tracer(0)
#t = turtle.Turtle()
#def koch(n, d):
#    if n == 1:
#        t.fd(d)
#    else:
#        koch(n-1, d/3)
#        t.lt(45)
#        koch(n-1,d/3)
#        t.rt(90)
#        koch(n-1, d/3)
#        t.lt(45)
#        koch(n-1,d/3)
#n = 5
#x = 4
#d = 300
#for j in range(1,21):
#    t.pu()
#    t.setpos(-12*j, 12*j)
#    t.pd()
#    for i in range(x):
#        koch(n,15*j)
#        t.rt(360/x)
#    turtle.update()
#turtle.exitonclick()

# priklad 7 - fraktaly (slozene se zmensenych kopii sebe sama)

def drak(n, s, u=90):
    if n == 0:
        t.fd(s)
    else:
        drak(n - 1, s, 90)
        t.lt(u)
        drak(n - 1, s, -90)
turtle.tracer(50,0)
t = turtle.Turtle()
t.pu()
t.setpos(100,220)
t.pd()
drak(14, 4)
turtle.exitonclick()
