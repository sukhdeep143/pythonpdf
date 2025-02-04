# factorial
#with the help of function perform arithmcatic function perform
#Sweping the value of a to b, b to a


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# n = int(input("Enter a number to find factorial of the number: "))
# print(factorial(n))


def arithmetic_operation(a,b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b

# num1 = int(input("Enter the first num1: "))
# num2 = int(input("Enter the second num2: "))
# operation = input("What you want to do with number: add, subtract or multiply: ")

# result = arithmetic_operation(num1, num2, operation)

# print(result)