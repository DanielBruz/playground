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


# cisla = [1,2,3,4,5,6,7,8,9,10]
# print(najdi_suda(cisla))

print(list_cisel())

def vytvor_list ():
	list = []
	n = int(input("Zadej delku pole: "))
	for i in range(0,n):
		item = int(input("Vloz znak: "))
		list.append(item)
	return list

pole = []	
pole = vytvor_list()
print("novy seznam je: ", pole)
print(sum(pole))
print(max(pole))
print(min(pole))
print(len(pole))

print("\n Uloha 4")

def delka(text):
	pocet = 0
	for znak in text:
		pocet += 1
	return pocet

print(delka("ahoj vsichni"))

print("\n Uloha 5")

def suda_cisla(cisla):
	suda = [cislo for cislo in cisla if cislo % 2 == 0]
	return suda

cisla = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]
print(suda_cisla(cisla))