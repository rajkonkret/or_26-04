# while - petla bez licznika
# sterowana warunkiem

# # pętla nieskonczona
# while True:
#     print("Komunikat")

licznik = 0
while True:  # zawsze prawda True - z dużej litery
    licznik += 1  # licznik = licznik + 1
    print("Komunikat")
    if licznik > 10:
        break  # przerywa bieżacą pętle

print(licznik)
licznik = 0
while licznik < 10:
    print("Komunikat...")
    licznik += 1

lista = []
while True:
    wej = input("Podaj liczbe")
    if not wej.isnumeric():
        break
    lista.append(wej)

print(lista)
# 11:20