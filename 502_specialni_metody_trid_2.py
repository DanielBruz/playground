class Prasiatko:
    def __init__(self, mince):
        self.mince = mince
    def celkova_suma(self):
        return sum(self.mince)
    def __lt__(self, ine_prasiatko):
        suma1 = self.celkova_suma()
        suma2 = ine_prasiatko.celkova_suma()
        return suma1 < suma2
    def __gt__(self, ine_prasiatko):
        suma1 = self.celkova_suma()
        suma2 = ine_prasiatko.celkova_suma()
        return suma1 > suma2
    def __eq__(self, ine_prasiatko):
        suma1 = self.celkova_suma()
        suma2 = ine_prasiatko.celkova_suma()
        return suma1 == suma2

p1 = Prasiatko([1, 1, 2, 2, 0.50])
p2 = Prasiatko([1, 1, 2, 2, 0.50, 0.20, 0.05])
