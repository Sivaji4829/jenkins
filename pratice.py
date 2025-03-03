def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Python Calculator")
    print("Operations: +  -  *  /")
    
    while True:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print(f"Result: {add(num1, num2)}")
        elif operator == "-":
            print(f"Result: {subtract(num1, num2)}")
        elif operator == "*":
            print(f"Result: {multiply(num1, num2)}")
        elif operator == "/":
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid operator! Please try again.")

        next_calc = input("Do you want to calculate again? (yes/no): ").lower()
        if next_calc != 'yes':
            print("Goodbye!")
            break

calculator()