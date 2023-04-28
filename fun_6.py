# funkcja, ktora oblicza srednia
def liczby(c, *cyfra):
    print(c)
    print(cyfra)
    suma = 0
    for cy in cyfra:
        suma += cy
    count = len(cyfra)
    print(suma)
    try:
        print(f"średnia dla id: {c} wynosi {suma / count}")
    except ZeroDivisionError:
        print("Nie dziel przez zero")


liczby(1)  # cyfra ile ma elementów?
liczby(1, 2, 3, 4, 5, 6, 7, 6, 7, 8, 93942, 4325525, 252523523, 235525453356)
