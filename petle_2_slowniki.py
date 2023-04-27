dictionary = {'imie': 'Radek', 'nazwisko': 'Kowalski'}

print(dictionary)

# zwaca klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)

# k, v to nasza nazwa zmiennej. dowolna w ramach PEP8
for k, v in dictionary.items():
    print(k, "=>", v)

# utworzyc słownik i wypisac klucze, wartosci, itemy do wyboru
dict_1 = {'name': 'imie', 'company': 'Orange'}
for k, v in dict_1.items():
    print(k, "=>", v)

print(dict_1)
# zamiana kluczy w słowniku z wartosciami - utworzyło nowy słownik
print({value: key for key, value in dict_1.items()})
dict_2 = {}
for key, value in dict_1.items():
    dict_2[value] = key
# value, key = key, value
print(dict_2)

