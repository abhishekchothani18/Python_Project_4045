# Define lambda functions
add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# Invoke appropriate lambda
if op == '+':
    print("Result:", add(num1, num2))
elif op == '-':
    print("Result:", sub(num1, num2))
elif op == '*':
    print("Result:", mul(num1, num2))
elif op == '/':
    if num2 != 0:
        print("Result:", div(num1, num2))
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
