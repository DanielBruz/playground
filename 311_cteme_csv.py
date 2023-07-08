print("csv 1")

oddelovac = ","
tabulka = []
with open("movies.csv", "r") as fp:
	for radek in fp:
		radek = radek.rstrip()
		tabulka.append(radek.split(oddelovac))
print(tabulka)

#print("csv 2")

#tabulka = []
#with open("movies.csv", "r") as fp:
#    reader = csv.reader(fp)
#    for riadok in reader:
#        print(riadok)
        
#print("csv 3")

#tabulka = []
#with open("movies.csv", "r") as fp:
#    reader = csv.DictReader(fp)
#    for riadok in reader:
#        print("{:.<60} {}".format(riadok["Title"],riadok["Rating"]))
