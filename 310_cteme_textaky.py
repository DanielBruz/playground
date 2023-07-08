print("Soubory 1")

soubor = open("soubor.txt", "r")
radek = soubor.readline().rstrip()
while radek:
    print(radek)
    radek = soubor.readline()
    if radek == "\n":
    	radek = " "
    	continue
    else:
    	radek = radek.rstrip()
# uzavreni souboru TXT
soubor.close()

print("Soubory 2")

soubor = open("soubor.txt", "r")
text = []
text = soubor.readlines()
soubor.close()
print(text)

print("Soubory 3")

with open("soubor.txt", "r") as fp:
    for line in fp:
        print(line.rstrip())
        
print("Soubory 4")

soubor = open("soubor.txt", "r")
text = ""
text = soubor.read()
soubor.close()
print(text)

print("Soubory 5")

import random
soubor = open("cisla.txt", "w")
for i in range(10):
    nahodne = random.randint(1,100000)
    soubor.write("cislo {} => {}\n".format(i,nahodne))
soubor.close()