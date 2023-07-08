print("Uloha 1")

a = 10
b = 14
c = ((a**2)+(b**2))**0.5
print(c)

print("Uloha 2")

velke_cislo = int(input("Zadej velke cislo: "))
posledni_tri = str(velke_cislo%1000)
print("Posledni tri cisla jsou: ", posledni_tri[0], ", ", posledni_tri[1], ", ", posledni_tri[2], ".")

print("Uloha 3")

dice1 = "{: ^7}".format('0')
dice2 = "{: <7}".format('0')
dice3 = "{: >7}".format('0')
dice4 = "{: ^7}".format('0     0')
dice5 = "{: ^7}".format(' ')

cislo = int(input("Vloz cislo na kostce: "))

if (cislo == 1):
    print("+" + 7*"-" + "+\n" + "|" + dice5 + "|\n" + "|" + dice1 + "|\n" + "|" + dice5 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 2):
    print("+" + 7*"-" + "+\n" + "|" + dice2 + "|\n" + "|" + dice5 + "|\n" + "|" + dice3 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 3):
    print("+" + 7*"-" + "+\n" + "|" + dice2 + "|\n" + "|" + dice1 + "|\n" + "|" + dice3 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 4):
    print("+" + 7*"-" + "+\n" + "|" + dice4 + "|\n" + "|" + dice5 + "|\n" + "|" + dice4 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 5):
    print("+" + 7*"-" + "+\n" + "|" + dice4 + "|\n" + "|" + dice1 + "|\n" + "|" + dice4 + "|\n" + "+" + 7*"-" + "+\n")
elif (cislo == 6):
    print("+" + 7*"-" + "+\n" + "|" + dice4 + "|\n" + "|" + dice4 + "|\n" + "|" + dice4 + "|\n" + "+" + 7*"-" + "+\n")
else:
    print("Nevlozil si spravne cislo!")


print("Uloha 4")

jmeno = input("Zadej sve jmeno a prijmeni: ")
vek = int(input("Zadej svuj vek: "))
adresa = input("Zadej svuj stat: ")

print("="*25)
print("Jmeno:" + "\t", jmeno)
print("Vek:" + "\t", vek)
print("Stat:" + "\t", adresa)
print("="*25)