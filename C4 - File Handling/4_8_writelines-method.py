file = open("data.txt", "w")

lines = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a programming language.",
    "File handling is important.",
]

file.writelines(lines)
file.close()