class Human:
    """
    klasa Human
    """

    def __init__(self, imie, wiek, plec='k'):  # własny konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec


cz_1 = Human("Monika", 56)
print(cz_1.imie)
cz_2 = Human("Radek", 65, 'm')
print(cz_2.imie)
print(cz_1.plec)
print(cz_2.plec)
