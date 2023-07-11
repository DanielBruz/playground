print("Uloha 1")

# Zeptat se na jméno souboru
nazev_souboru = input("Zadejte jméno souboru: ")

try:
    # Otevřít soubor pro čtení
    with open(nazev_souboru, 'r') as soubor:
        # Přečíst první řádek
        prvni_radek = soubor.readline()
        # Získat první 3 znaky
        prvni_tri_znaky = prvni_radek[:3]
        # Vypsat první 3 znaky
        print("První 3 znaky z prvního řádku:", prvni_tri_znaky)
except FileNotFoundError:
    print("Soubor nenalezen.")

print("Uloha 2")

# Zeptat se na jméno souboru
nazev_souboru = input("Zadejte jméno souboru: ")

try:
    # Otevřít soubor pro čtení
    with open(nazev_souboru, 'r') as soubor:
        # Přečíst všechny řádky souboru
        radky = soubor.readlines()

        # Počet řádků
        pocet_radku = len(radky)

        # Délka nejdelšího řádku
        nejdelsi_delka = max(len(radek) for radek in radky)

        # Výpis výsledků
        print("Počet řádků:", pocet_radku)
        print("Délka nejdelšího řádku:", nejdelsi_delka)

except FileNotFoundError:
    print("Soubor nenalezen.")

print("Uloha 3")

import csv
import os

def add_year(file_path):
    # Získání cesty k novému souboru
    directory = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(base_name)
    new_file_path = os.path.join(directory, f"{file_name}_with_year{file_ext}")

    # Otevření původního souboru pro čtení a nového souboru pro zápis
    with open(file_path, 'r', newline='') as input_file, open(new_file_path, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Přečtení záhlaví původního souboru
        header = next(reader)
        header.append("Year")

        # Zápis záhlaví do nového souboru
        writer.writerow(header)

        # Přidání sloupce Year s odpovídajícími hodnotami
        for row in reader:
            title = row[2]
            year = title[-5:-1]  # Získání roku z názvu filmu
            row.append(year)

            # Zápis řádku do nového souboru
            writer.writerow(row)

    print("Nový soubor byl vytvořen:", new_file_path)


# Příklad použití funkce
add_year("movies.csv")

print("Uloha 4")

import csv

CSV_FILE = "movies_with_year.csv"

def movies_by_year(year):
    found_movies = []

    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)

        # Přeskočení záhlaví
        next(reader)

        # Procházení řádků a hledání filmů s daným rokem
        for row in reader:
            movie_title = row[2]
            movie_year = row[4]

            if movie_year == str(year):
                found_movies.append(movie_title)

    # Výpis nalezených filmů
    if found_movies:
        print(f"Filmy z roku {year}:")
        for movie in found_movies:
            print(movie)
    else:
        print(f"Žádné filmy nebyly nalezeny z roku {year}.")

# Příklad použití funkce
movies_by_year(1958)
