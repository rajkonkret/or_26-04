# słownik - klucz, wartosc  - {"name":"radek"}
dict = {}  # pusty słownik

print(type(dict))  # <class 'dict'>
# 13:25
dict['imie'] = "Radek"
print(dict)
dict['wiek'] = 39
print(dict)

print(dict.values())
print(dict.keys())
print(dict.items())
dict.update({'data': '12-12-2023'})
print(dict)
dictionary = {'x': 2}
print(dictionary)
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)

dict_2 = {'imie': 'name', 'kot': 'cat'}
print(dict_2['imie'])
print(dict_2['kot'])
# ctrl / - komentarz zaznaczonych linii
# print("Mamy w słowniku", dict_2.keys())
# key = input("Podaj słowko do przetłumaczenia")  # input - wczytuje dane (str)
# print(dict_2[key.lower().replace(" ", "")])

a = input("Podaj liczbe a")
b = input("Podaj liczbe b")
print(int(a) + int(b))  # rzutowanie na int, mogłoby byc float()
