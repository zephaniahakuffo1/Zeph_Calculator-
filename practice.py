# # #get two numbers from the user

# def get_number(num1,num2):
#     num1=float(input("Enter your first number : " ))
#     num2=float(input("Enter your second number : "))
# get_number("","")
#  #let user choose operation
# def get_operation():
#     user_operation =input("Choose the operation you want to perform: + , - , * , / : ") 


# #performing of operations
# def add(num1, num2):
#     return(num1,num2)

# def subtract(num1,num2):
#     return(num1,num2)

# def multiply(num1,num2):
#     return(num1,num2)

# def divide(num1,num2):
#     return(num1,num2)

# #Display a welcome message

# print("Welcome to Zeph's Calculator".center(50))

# while True:
#     try:
#         get_number()
#         if num1 or num2 !=



def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /): ")
        if op in ["+", "-", "*", "/"]:
            return op
        else:
            print("Invalid operation")


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


def main():
    print("Welcome to Zeph's Calculator".center(70))

    num1 = get_number("Enter your first number: ")
    num2 = get_number("Enter your second number: ")

    operation = get_operation()

    result = calculate(num1, num2, operation)

    print(f"The result is: {result}")

main()

