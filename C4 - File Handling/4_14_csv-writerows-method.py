import csv

file = open("data.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["id", "name", "age", "address"])
writer.writerows([
    [1, "John Doe", 25, "123 Main St"],
    [2, "Jane Smith", 30, "456 Elm St"],
    [3, "Bob Johnson", 35, "789 Oak St"],
    [4, "Alice Brown", 28, "101 Pine St"],
    [5, "Charlie Green", 40, "202 Maple St"]
])

file.close()