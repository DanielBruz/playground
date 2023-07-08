i = 0
j = 0
rot = 3
sifra = ""
desifr = ""

zadani = input("Chces [s]ifrovat nebo [d]esifrovat?")

if (zadani == "s") or (zadani == "sifrovat"):
    text = input("Zadej text: ")
    delka = len(text)
    for i in range(delka):
        a = ord(text[i]) + rot
        sifra = sifra + chr(a)
    print("Sifra: ", sifra)
    print()

elif (zadani == "d") or (zadani == "desifrovat"):
    sifra = input("Zadej sifru: ")
    delka = len(sifra)
    for j in range(delka):
        b = ord(sifra[j]) - rot
        desifr = desifr + chr(b)
    print("Text: ", desifr)
    print()
