num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
num3 = int(input("Enter a number"))

if num1 > num2 and num1 > num3:
    print("Num1 is greater than all")
elif num2 > num1 and num2 > num3:
    print("Num2 is greater than all")
else:
    print("Num3 is greater")
    
