class Dom:
    """
    Klasa opisujaca Dom w Pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz  # pole prywatne
        self.kolor = kolor
        self.liczba_okien = liczba_okien

    def zmien_metraz(self):
        wybor = int(input("Podaj metraż"))
        self.__metraz = wybor
        print("Metraż wynosi", self.__metraz)


dom_1 = Dom(100, "zielony", 8)
print(dom_1.metraz) # bo pole zrobilismy prywatne __metraz
dom_1.metraz = 230
print(dom_1.metraz)
dom_1.zmien_metraz()
