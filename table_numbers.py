width = int(input("Zarovnej tabulku na: "))
print("-"*53)
for num in range(0,16):

    for base in "dbox":

        print("|  {0:{width}{base}}    ".format(num, base=base, width=width), end=' ')

    print("|")
print("-"*53)
