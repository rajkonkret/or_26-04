import json

# {'name':'Radek'} - typowy json - w pythonie jak słownik

person_dict = {'name': 'Radek', 'age': 39, 'czy_pali': None}
print(person_dict)

with open('dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open('dane.json', 'r') as json_f:
    data = json.load(json_f)

print(data)
print(data['name'])
print(data.keys())