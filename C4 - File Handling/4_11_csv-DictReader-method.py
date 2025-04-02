import csv

file = open("sample.csv", "r")

reader = csv.DictReader(file)

for row in reader:
    print(row["id"], row["name"], row["age"], row["address"])

file.close()