import csv

file = open("data.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["id", "name", "age", "address"])
writer.writerow([1, "John Doe", 25, "123 Main St"])
writer.writerow([2, "Jane Smith", 30, "456 Elm St"])
writer.writerow([3, "Bob Johnson", 35, "789 Oak St"])
writer.writerow([4, "Alice Brown", 28, "101 Pine St"])
writer.writerow([5, "Charlie Green", 40, "202 Maple St"])

file.close()