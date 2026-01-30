def arithmetic_calculator(num1, num2, operator):
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator. Use +, -, *, or /"

print("Simple Calculator")

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

result = arithmetic_calculator(a, b, op)
print(f"\nResult: {a} {op} {b} = {result}")
