print("\n Uloha 6")

zoznam_miest = [("Slovensko","Bratislava"), ("Maďarsko", "Budapešť"), ("Rakúsko","Viedeň")]
hlavne_mesta = dict(zoznam_miest)
print(hlavne_mesta)
print(type(hlavne_mesta))

mesta = list(hlavne_mesta.items())
print(mesta)

print("\n Uloha 7")

sk_en = {"cesta": "road", "zlato": "gold"}
slovnik = sk_en.copy()
print(sk_en, "\n")

slovnik["cesta"] = "path"
print(slovnik, "\n")

sk2 = {"cesta": "road", "zlato": "gold", "ahoj": "hi"}
slovnik.update(sk2)
print(slovnik, "\n")

for kluc in slovnik:
    print("slovnik[{}] => {}".format(kluc, slovnik[kluc]))

print()

for kluc in slovnik.keys():
    print("slovnik[{}] => {}".format(kluc, slovnik[kluc]))

print()

for hodnota in slovnik.values():
    print("slovnik[??] => {}".format(hodnota))

print()

for kluc, hodnota in slovnik.items():
    print("slovnik[{}] => {}".format(kluc, hodnota))
