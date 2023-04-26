# set , zbior - przechowuje niepowtarzajace sie elementy
lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamiana listy na set

print(lista)
print(zbior)
zb_2 = set()  # pusty set
zbior.add(33)
print(zbior)
zbior.add(18)
print(zbior)
print(zbior.pop())  # usuniecie i pobranie pierwszego elemntu
print(zbior.pop())
print(zbior.pop())
print(zbior)

zbior.remove(55)  # usuniecie po wartosci
print(zbior)
lista_2 = list(zbior)
print(lista_2)

zbior_2 = {66, 11, 44, 18, 52, 62, 999}
print(zbior_2)
print(zbior | zbior_2)  # suma zbiorów (or)
print(zbior & zbior_2)  # czesc wspolna zbiorów (and)
print(zbior - zbior_2)  # różnica zbiorów (diff)
print(zbior.difference(zbior_2))
