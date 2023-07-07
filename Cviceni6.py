# cisla = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# nove_cisla = [x for x in cisla if x % 2 == 0]
# print(nove_cisla)

# cisla = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# nove_cisla = [int(x) for x in cisla if x > 0]
# print(nove_cisla)

veta = "the quick brown fox jumps over the lazy dog"
slova = veta.split()
slova_delka = []

slova_delka = [len(x) for x in slova if x != "the"]

# for slovo in slova:
#       if slovo != "the":
#           slova_delka.append(len(slovo))

print(slova_delka)
