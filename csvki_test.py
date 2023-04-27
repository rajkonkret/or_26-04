import csv

# 14:20
# plik csv, to jest plik w którym dane oddzielone sa znakiem przestankowym
# Radek, Zenek, Tomek

fields = ['name', 'branch', 'year', 'cgpa']
rows = ['radek', 'COE', '2', '9.1']  # przykład danych w pythonie zgodny z kolumnami
my_dict_list = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Nikhil', 'year': '2'},
    {'branch': 'COP', 'cgpa': '9', 'name': 'Radek', 'year': '3'},
]

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields,  delimiter=';')
    csvwriter.writeheader()
    csvwriter.writerows(my_dict_list)





