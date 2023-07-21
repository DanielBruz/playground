
import datetime
class Zamestnanec:
    def __init__(self, meno, priezvisko, datum_narozeni):
        self.meno = meno
        self.priezvisko = priezvisko
        self.cele_meno = meno + " " + priezvisko
        self.datum_narozeni = datum_narozeni    #yyyymmdd
    def vek(self):
        rok = int(self.datum_narozeni[0:4])
        mesic = int(self.datum_narozeni[4:6])
        den = int(self.datum_narozeni[6:8])
        narozeny = datetime.date(rok, mesic, den)
        dnes = datetime.date.today()
        pocet_dni = (dnes - narozeny).days
        vek = pocet_dni // 365
        return vek
    def __str__(self):
        vek = str(self.vek())
        viz = "=======================\n"
        viz += "{}: {} roku\n".format(self.cele_meno, vek)
        viz += "=======================\n"
        return viz

vratnik = Zamestnanec("Tomas", "Murcina", "19880417")