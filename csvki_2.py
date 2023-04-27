import csv

filename = 'records.csv'

fileds = []
rows = []

with open(filename, 'r') as csv_f:
    csvreader = csv.reader(csv_f, delimiter=';')

    fileds = next(csvreader)  # ustawia wskaznik  na nastepny element
    for row in csvreader:
        rows.append(row)

print(fileds)
print(rows)