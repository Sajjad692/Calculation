# Step 1: Take two numbers from the user
num1=float(input("Enter first Number: "))
num2=float(input("Enter second Number: "))
# Step 2: Show the user what operation they can use
print("Choose Operations: +, -, *, /")
# Step 3: User choice for operations
operation=input("Enter Operations:")
# Step 4: Use if-elif to perform the correct calculations
if operation == "+":
    print("Result:",num1+num2)
elif operation == "-":
    print("Result:",num1-num2)
elif operation == "*":
    print("Result:",num1*num2)
elif operation =="/":
    print("Result:",num1/num2)
else:
    print("Invalid Operation")