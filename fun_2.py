# z return funkcja zwróci nam wynik
def dodaj(a, b):
    return a + b


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))
print(dodaj(5, 6) + dodaj(7, 8))
print(oblicz_vat(1000, 23))
i = 8
j = 19
print(dodaj(i, j))
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
