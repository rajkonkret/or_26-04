class Human:
    """
    klasa Human
    """

    def __init__(self, imie, wiek, plec='k'):  # własny konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print(self)
        """
        metoda witająca
        :return: wypisuje  
        """
        print("Nazywam się", self.imie)

    def ruszaj(self):
        if self.plec == 'k':
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz_1 = Human("Monika", 56)
print(cz_1.imie)
cz_2 = Human("Radek", 65, 'm')
print(cz_2.imie)
print(cz_1.plec)
print(cz_2.plec)
cz_2.ruszaj()
