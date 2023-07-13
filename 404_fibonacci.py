# Fibonacciho posloupnost: 1,1,2,3,5,8,13,21,...

# priklad 1 - s rekurzi

#def fib(n):
#    if n < 2:       #  definice trivialniho pripadu, kdyz je n = 0 nebo 1
#        return 1
#    else:
#        return fib(n-1)+fib(n-2)    # vrati soucet dvou predchozich prvku
#for i in range(100):
#    print("fib({}) => {}".format(i,fib(i)))

# priklad 2 - spocitejme, kolikrat se zavola funkce Fib()

#count = 0
#def fib(n):
#    global count
#    count += 1
#    if n < 2:
#        return 1
#    else:
#        return fib(n-1)+fib(n-2)
#x = fib(30)
#print(x)
#print("funkce fib sa zavolala {}".format(count))

# priklad 3 - abychom porad nepocitali to same, zkusme si zapamatovat uz vypocitane hodnoty
# a nez volame rekurzi, podivejme se do ulozenych hodnot

#fib_cache = {}
#def fib(n):
#    if n in fib_cache:
#        return fib_cache[n]
#    if n < 2:
#        return 1
#    else:
#        x = fib(n-1)+fib(n-2)
#        fib_cache[n] = x
#        return x
#for i in range(100):    # cyklus, ktery mi vypocita fib pro prvnich 100 cisel
#    print("fib({}): {}".format(i, fib(i)))
#print("fib(300): {}".format(fib(300)))  # zkusmo vypocitejme fib pro 300

# priklad 4 - pouzijme pro takove pripady tzv. dekorator (LRU - last recently used)

from functools import lru_cache
@lru_cache(maxsize=1000)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(100):
    print("fib({}): {}".format(i, fib(i)))
print("fib(300): {}".format(fib(300)))
