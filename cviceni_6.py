print("\n Uloha 1")

cisla = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nove_cisla = [x for x in cisla if x % 2 == 0]
print(nove_cisla)

print("\n Uloha 2")

cisla = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
nove_cisla = [int(x) for x in cisla if x > 0]
print(nove_cisla)

print("\n Uloha 3")

veta = "the quick brown fox jumps over the lazy dog"
slova = veta.split()
slova_delka = []

slova_delka = [len(x) for x in slova if x != "the"]

# for slovo in slova:
#       if slovo != "the":
#           slova_delka.append(len(slovo))

print(slova_delka)

print("\n Dalsi testy")

slova = ['the','quick','brown','fox','jumps','over','the','lazy','dog']
delimiter = " "
veta = delimiter.join(slova)
print(veta)

veta = "the quick brown fox jumps over the lazy dog"
slova = veta.upper().split(" ")
print(slova)

veta2 = ""
for slovo in slova:
	veta2 = veta2 + slovo.lower() + " "
veta2 = veta2.strip()
print(veta2)
print(len(veta2))
print(veta2.count(""))



