kurs_dol = 4.16
kurs_eur = 4.58


def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota):
        print("Przeliczam dolary", kurs_dol * kwota)

    def eur(kwota):
        print("Przeliczam euro", kurs_eur * kwota)

    if waluta.upper() == "EUR":  # zamiana na duze litery, by nie wpsc w pułapke duze/małe litery
        return eur
    else:
        return usd


# kantor ma przeliczac konkretne kwotny
# pobrac kwote od klienta (input)
# zmodyfikowac funkcje usd,eur tak by przyjmowały kwote w argumentach(dodaj(a))
# wypisac przeliczone kwoty
# 4,58 pln/eur
# 4,16 pln/usd
waluta = input("Podaj walute eur/usd")
kwota = int(input("Podaj kwote do wymiany"))
moj_kantor = kantor(waluta)
print(moj_kantor)
moj_kantor(kwota)
