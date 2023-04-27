# odp = True
#
# if odp:
#     print("Brawo")
#
# # czy_znasz_pythona = 'n'
# czy_znasz_pythona = input("Czy znasz pythona (t/n)")
# if czy_znasz_pythona.lower().replace(" ", "") == 't':  # == - porównanie
#     print('Brawo')
# else:  # w przeciwnym przypadku
#     print("Idź się uczyc")
#
# print("Dalsza częśc programu")

# podatek = 0.0
# zarobki = int(input("Dochod"))  # str na int bo  input zawsze zwraca str
# if zarobki < 10000:
#     podatek = 0.02
# elif zarobki < 30000:
#     podatek = 0.1
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
#
# print(f"Zapłącisz {zarobki * podatek} zł")

# suma_zam = 150
# if suma_zam > 100:
#     rabacik = 25
# else:
#     rabacik = 0
#
# print(f"Rabacik {rabacik}")
#
# rabat = 25 if suma_zam > 100 else 0
# print(f"Rabacik {rabat}")

lista_bledow = []
alert_system = 'email'
error = 'critical'
error_message = "Stało się coś strasznego"

if alert_system == 'console':
    print(error_message)
elif alert_system == "email":
    if error == 'medium':
        lista_bledow.append('medium')
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('nieznany')

print(lista_bledow)

# test z historii. conajmniej jedno pyanie i sprawdzenie odpowiedzi od uzytkownika.
# Chrzest Polski w 966

# 1. Pokazanie pytania uzytkownikowi
# 1a. Pobranie odpowiedzi
# 2. Sprawdzenie odpowiedzi
# 3. Ogłoszenie wyniku testu

# odp = int(input('Podaj date Chrztu Polski'))
odp = input('Podaj date Chrztu Polski')
if odp == '966':
    print("Prawidłowa odpowiedź")
else:
    print("Masz w książce na 23 stronie ;)")

# hackerrank
