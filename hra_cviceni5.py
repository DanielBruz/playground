import random

jmeno = input("Zadej jmeno hrace: ")
if jmeno == "":
    jmeno = "player"

print("Ahoj {}".format(jmeno))

cislo = random.randint(1, 10)
zadani = input("Zadej cislo 1 az 10, ktere si myslim: ").lower().strip()

spatne = 0
dobre = 0

while zadani != "konec":
    if zadani.isdigit():
        zadani = int(zadani)
    else:
        print("Zadavej cisla a ne znaky!")
        print("Spust si program znovu.")
        break
    if zadani > 10:
# zaporna cisla bere jako string
        print("Prosim zadavej cisla 1 az 10")
        print("Tento pokus se nepocita.")
        spatne -= 1
    if zadani != cislo:
        zadani = input("Zkus to znovu: ").lower().strip()
        spatne += 1
    if zadani == cislo:
        zadani = input("Uhodl jsi :-) Zkus to jeste: ").lower().strip()
        dobre += 1
        cislo = random.randint(1, 10)
print()
print("Konec hry")
print("\n+-----------tvoje skóre------------+")
print("| Pocet chybnych pokusu:  | {:^7}|".format(spatne))
print("| Pocet spravnych pokusu: | {:^7}|".format(dobre))
print("| Pocet pokusu celkem:    | {:^7}|".format(spatne + dobre))
print("+==================================+")