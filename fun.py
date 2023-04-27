# funkcje
# wydzielona czesc kodu, ktorą można wywoływac wielokrotnie
a = 10
b = 5


def dodaj():  # definicja/deklaracja funkcji
    print(a + b)


def dodaj_2(a, b):
    print(a + b)


def odejmij(a, b, c=0):
    print(a - b - c)


def mnozenie(a, b):
    print(a * b)


def dzielenie(a, b):
    try:
        print(a / b)  # dzielenie w wyniku zwraca zawsze float
    except ZeroDivisionError:
        print("Nie dzielimy przez zero")


dodaj()  # wywołąnie funkcji
dodaj_2(5, 6)  # dla tej funkcji argumenty są obowiązkowe
odejmij(9, 7)  # nie podano c, wiec przyjmie wartoś domyślną z deklaracji funkcji
odejmij(9, 7, 5)  # podalismy c=5
mnozenie(6, 8)
dzielenie(2, 0)
dzielenie(5, 4)
print(9 // 4)  # częśc całkowita z dzielenia
print(9 ** 4)  # potęgowanie
mnozenie(b=8, a=7)  # argumenty przekazane po nazwie, nie treba achowywac kolejności
odejmij(c=7, b=8, a=7)

print(dodaj())  # zwraca None
