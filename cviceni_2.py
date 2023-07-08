

forma = "{0:0>32b}"
print(forma.format(int(input("vloz cislo k prevodu do binaru: "))))


width = int(input("Vloz sirku zarovnani: "))
cstr = "dec"
cstr2 = "bin"
cstr3 = "oct"
cstr4 = "hex"
cstr5 = "Tabulka ciselnych soustav"

print()

print("+" + cstr5.center(width*5+4, '-') + "+")
print ("+" + cstr.center(width+4, '-') + "+" + cstr2.center(width+4, '-') + "+" + cstr3.center(width+4, '-') + "+" + cstr4.center(width+4, '-') + "+")
print("+" + "-"*(width*4 + 19) + "+")

for num in range(0, 16): 
    for base in "dbox":
        print("| 0{base}{0:<{width}{base}}".format(num, base = base, width = width), end=" ")
    print("|")

print("+" + "-"*(width*4 + 19) + "+")
