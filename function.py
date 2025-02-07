# def add(a,b):
#     return a+b


# print(add(4,5))


def sumType(a,b,what_you_want_todo):
    if what_you_want_todo == "add":
        return a + b
    elif what_you_want_todo == "sub":
        return a - b
    elif what_you_want_todo == "dev":
        return a / b
    else:
        print("Give some real value's")
        

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
opration_type = input("What type of opration you want to do: 'add', 'sub', 'dev': ")

result = sumType(num1, num2, opration_type)

print(result)
