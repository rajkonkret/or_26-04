# klasa - szablon, opis w jaki sposób konstrujemy obiekt
class Human:
    """
    To jest klasa Human opisująca człowieka w Pythonie
    """
    liczba_palcow = 20
    kolor_wlosow = None
    imie = ""
    plec = "k"
    wiek = ""
    wzrost = None

    # self - obowiazkowe, działamy na obiekcie nie na klasie
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


cz_1 = Human()
print(cz_1.__doc__)
print(cz_1.imie)
cz_1.imie = "Radek"
print(cz_1.imie)
cz_1.plec = 'm'
print(cz_1.plec)
cz_1.powitanie()
cz_1.ruszaj()

cz_2 = Human()  # konstruktor domyslny, bezargumentowy
cz_2.imie = "Agnieszka"
print(cz_2.imie)
print(cz_2.plec)
cz_2.powitanie()  # tu juz bez self
cz_2.ruszaj()
