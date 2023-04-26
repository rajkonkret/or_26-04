# krotka, tupla - nimodyfikowalna, niemutowalna
# zmienna niezmienna
tupla = ("Tomek", "Asia", "Marek", "Paulina")  # tworzenie tupli
tupla_2 = ("Radek",)
tupla_3 = (43, 55, 22.42, 11, 200)
# ctrl alt l Reformat code Ctrl Alt L
print(type(tupla))
print(type(tupla_2))
print(type(tupla_3))
print(tupla.count("Tomek"))
print(tupla.index("Tomek"))
tp = 1, 2, 3
a, b, c = tp
print(a)
print(type(a))

a, *b, c = 1, 2, 5, 6, 7, 8, 9, 0, 3, 4  # rozpakowanie tupli
print(a)
print(b)
print(c)

a, *b, c, d = 1, 2, 3
print(a)
print(b)
print(c)
print(d)

imie_1, *imie_2, imie_3 = tupla
print(imie_2)

lista = list(tupla)  # zamiana tupli na liste
print(lista)
