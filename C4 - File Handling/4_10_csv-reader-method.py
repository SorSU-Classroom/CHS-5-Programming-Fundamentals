import csv

file = open("sample.csv", "r")

reader = csv.reader(file)

for row in reader:
    print(row)

file.close()