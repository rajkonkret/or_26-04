class Dom:
    """
    Klasa opisujaca Dom w Pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz  # pole prywatne
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def wypisz_metraz(self):
        print("Metraż wynosi", self.__metraz)

    def wypisz_kolor(self):
        print("Kolor", self.__kolor)

    def wypisz_okna(self):
        print("Liczba okien wynosi", self.__liczba_okien)

    def zmien_metraz(self):
        wybor = int(input("Podaj metraż"))
        self.__metraz = wybor
        print("Metraż wynosi", self.__metraz)

    def zmien_kolor(self):
        wybor = input("podaj kolor")
        self.__kolor = wybor
        print("Ustawiłeś kolor", self.__kolor)

    def zmien_okna(self):
        wybor = int(input("Podaj liczbe okien"))
        self.__liczba_okien = wybor
        print("Liczba okien wynosi", self.__liczba_okien)

    def __farba(self):  # __ - metoda prywatna
        print("Skonczyła sie farba koloru", self.__kolor)


dom_1 = Dom(100, "zielony", 8)
# print(dom_1.metraz) # bo pole zrobilismy prywatne __metraz
# dom_1.metraz = 230
# print(dom_1.metraz)
# print(dom_1.metraz)
dom_1.zmien_metraz()
dom_1.wypisz_metraz()
dom_1.wypisz_kolor()
dom_1.zmien_kolor()
# 13:25