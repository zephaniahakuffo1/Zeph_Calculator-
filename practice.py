print("         Welcome to Zeph's Calculator            ")        

#Ask the user for two valid inputs

while True :
    try:
        num1=float(input("Enter your first number:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True :
    try:
        num2=float(input("Enter your second number:"))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#Ask the user for the operation they want to perform
while True:

    operation=input("Enter the operation you want to perform (+, -, *, /):")

    if operation == "+":
        result=num1+num2
        break
        print(f"The result is : {result}")                      

    elif operation == "-":
        result=num1-num2
        break
        print(f"The result is : {result}")  

    elif operation == "*":
        result=num1*num2
        break
        print(f"The result is : {result}")  

    elif operation == "/":
        if num2==0:
            print("Error:division by zero is not possible")
            continue
        result=num1/num2
    else:
        print(f"Invalid operation , {operation}")
        continue

#Provide the results
print(f"The result is: {result}")

