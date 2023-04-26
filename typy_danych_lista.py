# lista  - kolekcja do przechowywania elemntow
lista = []  # deklaracja pustej listy

print(lista)
print(type(lista))  # <class 'list'>
lista.append("Radek")  # dodawanie elementu do listy na koncu listy
lista.append("Maciek")  # dodawanie elementu do listy
lista.append("Zenake")  # dodawanie elementu do listy
lista.append("Paweł")  # dodawanie elementu do listy
# ctrl d - powielenie lini
print(lista)

# indeksy w liscie sa numerowane od zera
print(lista[0])  # wyswietlenie pierwszego elementu z listy, indeks=0
print(lista[3])
print(lista[-2])
print(lista[-1])  # ostatni element z listy

# wstawienie elementu do listy na wskazanym indeksie
lista.insert(1, "Piotr")
print(lista)

# zastapienie elementu na indeksie 2
lista[2] = "Monika"
print(lista)

# usuniecie elemntu z listy
lista.remove("Piotr")
print(lista)

# usuniecie po indeksie i zwrocenie go nam
# ['Radek', 'Monika', 'Zenake', 'Paweł']
element = lista.pop(2)  # Zenake
print(element)
print(lista)  # ['Radek', 'Monika', 'Paweł']

# kopiowanie listy do drugiej listy
lista_copy = lista.copy()
print(lista_copy)

# kasowanie wsztytskich elemntow listy
lista.clear()
print(lista)
print(lista_copy)
print("Radek" in lista_copy)  # True - prawda, False - falsz
# 11:25

liczby = [54, 999, 34, 22, 12.54, 687]
print(liczby)
liczby.sort()
print(liczby)
liczby.reverse()
print(liczby)
liczby[2] = 6666
print(liczby)
print(liczby[0:3])  # wyswietla od indeksu 0 ... 2 ( 3 juz nie jest wyswietlany)
print(liczby[:-2])  # od -2 do 0
print(liczby[2:])  # od 2 do końca włącznie
liczby.remove(34)
print(liczby)
print(len(liczby))  # długosc kolekcji, liczba elementów

krotka = tuple(liczby)  # rzutowanie listy na tuple, konwersja typu
print(krotka)  # (999, 687, 6666, 22, 12.54)

print(type(krotka))  # <class 'tuple'>
