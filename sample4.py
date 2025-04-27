# while True:
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#
#         quotient = num1 // num2
#         print("Quotient:", quotient)
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except ValueError:
#         print("Error: Invalid input. Please enter a valid integer.")
#     except Exception as e:
#         print("Error: ", e)
#     finally:
#         print("This is the finally block. It always executes.")
#
#
# # fruits = ["apple", "banana", "cherry"]
# #
# # print(fruits[3])
#
# # person = {
# #     "name": "John",
# #     "age": 30,
# #     "city": "New York"
# # }
# #
# # print(person["birthdate"])

# try:
#     positive_number = int(input("Enter a positive number: "))
#
#     if positive_number < 0:
#         raise ValueError("The number must be positive.")
#
#     print("You entered:", positive_number)
# except ValueError as ve:
#     print("Error: ", ve)
# except Exception as e:
#     print("Error: ", e)

class InvalidAgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    elif age > 120:
        raise InvalidAgeError("Age cannot be greater than 120.")

    print("Your age is:", age)
except InvalidAgeError as iae:
    print("Error: ", iae)
except Exception as e:
    print("Error: ", e)