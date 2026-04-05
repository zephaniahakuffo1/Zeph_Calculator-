def add (a, b):
    return a + b            
def subtract (a, b):
    return a - b        

def multiply (a, b):
    return a * b    
def divide (a, b):          
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b                    
def main():
    print("Welcome to Zeph's Calculator".center(50))
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Invalid operation"

    print(f"The result is: {result}")

main()
    