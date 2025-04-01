file = open("sample.txt", "r")

lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()