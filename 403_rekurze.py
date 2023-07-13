# chvostova rekurze

# priklad 1

#import turtle
#turtle.delay(1000)
#t = turtle.Turtle()
#t.speed(0)
#def spirala(d):
#    print("volani spiraly({})".format(d))
#    if d > 100:
#        pass     # nerob nič
#        print("... trivialny pripad - nedelam nic")
#    else:
#        t.fd(d)
#        t.lt(60)
#        print("... rekurzivne volam spiralu({})".format(d+3))
#        spirala(d+3)
#        print("... navrat z volani spiraly({})".format(d+3))
#spirala(90)

# priklad 2 - prepis pomoci WHILE cyklu

#import turtle
#turtle.delay(1000)
#t = turtle.Turtle()
#t.speed(0)
#def spirala(d):
#    while d <= 100:
#        t.fd(d)
#        t.lt(60)
#        d = d + 3
#spirala(90)

# rekurze "bez chvostu"

# priklad 1

#import turtle
#import time

#turtle.delay(10)
#t = turtle.Turtle()
#t.speed(0)
#def spirala(d):
#    if d > 100:
#        t.pencolor("red")
#    else:
#        t.fd(d)
#        t.lt(60)
#        spirala(d+3)
#        t.fd(d)
#        t.lt(60)
#spirala(10)
#time.sleep(3)

# priklad 2

def cisla(n):
    if n < 1:
        pass
    else:
        print(n, end=', ')
        cisla(n - 1)
        print(n, end=', ')
cisla(10)
