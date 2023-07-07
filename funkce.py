# def kresli(znak, pocet):
#    print(znak*pocet)

# for i in range(10):
#    kresli("*", i)

# def dlzka(retazec):
#    pocet = 0
#    for znak in retazec:
#        pocet += 1
#    return pocet

# retazec = input("Vloz retazec: ")
# a = dlzka(retazec)
# print(a)

# def sude(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# n = int(input("Vlož cislo: "))
# print(sude(n))

# def preloz(slovo):
#    if slovo == "ahoj":
#         return 'hello'
#     elif slovo == "dovidenia":
#         return 'good bye'

# slovo = input("Vloz slovo: ")
# print(preloz(slovo))

def najdi_suda(cisla):
    suda_cisla = [cislo for cislo in cisla if cislo % 2 == 0]
    return suda_cisla

def list_cisel():
    cisla = []
    n = int(input("Vloz pocet cisel : "))
    for i in range(0, n):
        item = int(input())
        cisla.append(item)
    return cisla

vstup = []
vstup = list_cisel()
print(najdi_suda(vstup))
