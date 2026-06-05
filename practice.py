#function to get user number
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#function to get operation to use
def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in ["+", "-", "*", "/"]:
            return op
        else:
            print("Invalid operation")

#function to perform calculation
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: division by zero"
        return num1 / num2

#main function to run everything
def main():
    print("Welcome to Zeph's Calculator".center(70))

    num1 = get_number("Enter your first number: ")
    num2 = get_number("Enter your second number: ")

    operation = get_operation()

    result = calculate(num1, num2, operation)

    print(f"The result is: {result}")

main()






#redo of the calculator using  OOP  and adding more features

