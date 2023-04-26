import random

# bibloiteka do generowania liczb pseudolosowych

print(random.randint(1, 6))  # losuje int od 1 do 6
print(random.random() * 6)  # losuje flat od 0 do 1(bez 1) ale * 6 daje nam od zera do 5.999999
print(random.randrange(6))  # losuje od 0 do 5 całkowite
print(random.randrange(1, 6))  # od 1 do 5 całkowite

lista = [5, 7, 6, 45, 34, 56]
print(random.choice(lista))

# od 1 .. 49
lista_2 = list(range(1, 50))
print(lista_2)

lista_3 = []

wyn = random.choice(lista_2)
lista_2.remove(wyn)
print(wyn)
lista_3.append(wyn)
wyn = random.choice(lista_2)
lista_2.remove(wyn)
print(wyn)
lista_3.append(wyn)

wyn = random.choice(lista_2)
lista_2.remove(wyn)
print(wyn)
lista_3.append(wyn)

wyn = random.choice(lista_2)
lista_2.remove(wyn)
print(wyn)
lista_3.append(wyn)

wyn = random.choice(lista_2)
lista_2.remove(wyn)
print(wyn)
lista_3.append(wyn)

wyn = random.choice(lista_2)
lista_2.remove(wyn)
print(wyn)
lista_3.append(wyn)

print(lista_3)
