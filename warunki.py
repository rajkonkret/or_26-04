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

podatek = 0.0
zarobki = int(input("Dochod"))  # str na int bo  input zawsze zwraca str
if zarobki < 10000:
    podatek = 0.02
elif zarobki < 30000:
    podatek = 0.1
elif zarobki < 100000:
    podatek = 0.4
else:
    podatek = 0.6

print(f"Zapłącisz {zarobki * podatek} zł")
