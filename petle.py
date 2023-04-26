# petla for
import random

for i in range(10):  # 0 .. 9
    print(i)  # wciecie obowiazkowe

# pass - nic nie rób
# _ niema zmienna
for _ in range(10):
    pass

lista_p = []
for i in range(10):
    if i % 2 == 0:  # if - warunek, % - modulo, czyli reszta z dzielenia
        print("Jest parzysta")
        print(i)
        lista_p.append(i)

print(lista_p)

lista_2 = list(range(1, 50))  # 1.. 49
lista_3 = []

for i in range(6):
    wyn = random.choice(lista_2)
    lista_2.remove(wyn)
    print(wyn)
    lista_3.append(wyn)

print(lista_3)

lista_4 = [2, 7, 9, 10, 23, 45]

for cyfra in lista_4:
    if cyfra == 2:
        cyfra += 1  # cyfra = cyfra + 1
    print(cyfra)

lista_5 = [j for j in range(10) if j % 2 == 0]
print(lista_5)
# for i in range(10):
#     if i % 2 == 0:  # if - warunek, % - modulo, czyli reszta z dzielenia
#         print("Jest parzysta")
#         print(i)
#         lista_p.append(i)

imiona = ["Radek", "Zenek", "Marta"]

for p in imiona:
    print(p, end=', ')

print()
# 0 Radek, 1 Zenek
for p in range(len(imiona)):  # range(3) 0..2
    print(p, imiona[p])

# enumerate - ponumerowanie kolekcji i zrocenie indeksu i wartosci (p, w)
for p, w in enumerate(imiona):
    print(p, w)

ludzie = ["Radek", "Zenek", "Asia", "Michał"]
wiek = [47, 67, 32, 48]
jezyk = ['java', 'python']
for p, o in enumerate(ludzie):
    print(p, o)

for p, o in enumerate(ludzie):
    print(p, o, wiek[p])  # p - indeks

# zip - łączy kolekcje
for o, w, j in zip(ludzie, wiek, jezyk):
    print(o, w, j)

ind = list(range(len(ludzie)))
for i, o, w, j in zip(ind, ludzie, wiek, jezyk):
    print(i, o, w, j)

jezyk_2 = ['java', 'python', 'c++', 'perl']
for i1, (o2, w3, j4) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i1, o2, w3, j4)

for i1, (o2, w3, j4) in enumerate(zip(ludzie, wiek, jezyk_2)):
    print(i1, o2, w3, j4)
