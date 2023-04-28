from abc import ABC, abstractmethod


# klasa abstrakcyjna/interfejs - nie da sie stworzyc obiektu
class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lataj(self):
        print("Tu", self.gatunek, "Lecę z szybkościa", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    """
    To jest orzeł
    """

    def poluj(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiiii")


class Kura(Ptak):
    """
    To jest kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)
        self.gatunek = gatunek

    def lataj(self):
        print("Tu ", self.gatunek, ". Ja nie latam", sep='')

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")

    def wydaj_odglos(self):
        print("kokokokoko")


# or_1 = Ptak("orzel", 20)
# print(or_1.szybkosc)
# kura = Ptak("kura", 0)
or_2 = Orzel("orel", 50)
# or_1.lataj()
# kura.lataj()
or_2.lataj()
kur_2 = Kura("Kura")
kur_2.lataj()
kur_2.dziobanie()
or_2.poluj()
kur_2.wydaj_odglos()
