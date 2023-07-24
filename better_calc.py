num1 = float(input("Enter first number"))
num2 = float(input("Enter second Number"))
op = input("Enter Operator")

if op == "+":
    print(num1 + num2) 
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid Opereator")