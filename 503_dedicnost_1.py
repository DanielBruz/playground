import datetime


class Zamestnanec:
    def __init__(self, meno, priezvisko, datum_narodenia):
        self.meno = meno
        self.priezvisko = priezvisko
        self.cele_meno = meno + " " + priezvisko
        self.datum_narodenia = datum_narodenia

    def vek(self):
        rok = int(self.datum_narodenia[0:4])
        mesiac = int(self.datum_narodenia[4:6])
        den = int(self.datum_narodenia[6:8])
        nar = datetime.date(rok, mesiac, den)
        dnes = datetime.date.today()
        pocet_dni = (dnes - nar).days
        vek = pocet_dni // 365
        return vek

    def __str__(self):
        vek = str(self.vek())
        viz = "==========================\n"
        viz += "{}: {} rokov\n".format(self.cele_meno, vek)
        viz += "==========================\n"
        return viz


class Vratnik(Zamestnanec):
    def __init__(self, meno, priezvisko, datum_narodenia, email):
        super().__init__(meno, priezvisko, datum_narodenia)
        self.email = email

    def __str__(self):
        vek = str(self.vek())
        viz = "==========================\n"
        viz += "{}: {} rokov\n".format(self.cele_meno, vek)
        viz += "{}: {}\n".format("email", self.email)
        viz += "==========================\n"
        return viz

    def zmen_meno(self, meno):
        self.meno = meno
        self.cele_meno = meno + " " + self.priezvisko

