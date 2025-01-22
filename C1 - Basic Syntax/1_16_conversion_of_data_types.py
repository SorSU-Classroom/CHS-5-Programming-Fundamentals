x = 5
y = 3.14
z = '10'

list_numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
tuple_numbers = (1, 2, 3, 4, 5)
dict_colors = {'red': 255, 'green': 255, 'blue': 255}

print("Integer to Float:", float(x))
print("Float to Integer:", int(y))
print("String to Integer:", int(z))
print("List to Tuple:", tuple(list_numbers))
print("Tuple to List:", list(tuple_numbers))
print("Dictionary to List:", list(dict_colors))
print("List to Set:", set(list_numbers))
print("Integer to Boolean:", bool(x))
print("Integer to Character:", chr(65))