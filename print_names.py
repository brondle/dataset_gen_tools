import csv

print('[')
with open('columns.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(' "' + row[0] + '",')
print(']')
