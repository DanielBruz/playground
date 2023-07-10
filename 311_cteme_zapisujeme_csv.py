#import csv
#import random

#print("csv 1")

#oddelovac = ","
#tabulka = []
#with open("movies.csv", "r") as soubor:
#	for radek in soubor:
#		radek = radek.rstrip()
#		tabulka.append(radek.split(oddelovac))
#print(tabulka)

#print("csv 2")

#with open("movies.csv", "r") as soubor:
#	reader = csv.reader(soubor)
#	for radek in reader:
#		print(radek, "\n")

#print("csv 3")

#with open("movies.csv", "r") as soubor:
#	reader = csv.DictReader(soubor)
#	for radek in reader:
#		print("{:.<100} {}".format(radek["Title"],radek["Rating"]))

#print("csv 4")

#with open("cisla.txt", "w") as soubor:
#	for i in range(10):
#		nahodne = random.randint(1,100000)
#		soubor.write("cislo {} => {}\n".format(i,nahodne))

print("csv 5")

import csv
tabulka = []
with open("movies.csv", "r") as soubor:
	reader = csv.DictReader(soubor)
	for radek in reader:
		tabulka.append(radek)
print(tabulka)

nova_tabulka = []
for row in tabulka:
	nazev = row["Title"]
	samo = sum([nazev.count(samohlaska) for samohlaska in "aeiou"])
	delka = len(nazev)
	nova_tabulka.append([nazev, samo, delka])
print(nova_tabulka)

with open("moje_data.csv", "w") as fp:
	writer = csv.writer(fp, delimiter="*")
	writer.writerow(["text", "samohlasky", "delka"])
	for radek in nova_tabulka:
		writer.writerow(radek)

