def greet_user():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    print(f"Hello, {first_name} {last_name}!")

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_even_numbers():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i, "is even.")

# def greet():
#     print("Hello, User!")

def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     return x / y

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y

# print('''
# Select an Operation to perform:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# ''')
#
# operation = int(input("Enter your choice (1-4): "))
# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
#
# if operation == 1:
#     result = add(num1, num2)
#     print("Sum:", result)
# elif operation == 2:
#     result = subtract(num1, num2)
#     print("Difference:", result)
# elif operation == 3:
#     result = multiply(num1, num2)
#     print("Product:", result)
# elif operation == 4:
#     result = divide(num1, num2)
#     print("Quotient:", result)
# else:
#     print("Invalid choice!")

# def factorial(n):
#     for i in range(1, n):
#         n *= i
#     return n
#
# n = int(input("Enter a number: "))
# result = factorial(n)
# print(f"{n}! = {result}")

fruits = ["banana", "apple", "mango", "orange", "strawberry"]


# # print(min(list_numbers))
# book_title = "Harry Potter and the Philosopher's Stone"
# book_title_list = book_title.split(" ")
#
# print("-".join(book_title_list))

list_numbers = [5, 17, 37, 29, 11, 37, 729, 910]

print(list_numbers)