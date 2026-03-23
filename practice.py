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

operation=input("Enter the operation you want to perform (+, -, *, /):")


#perform the operations
if operation == "+":
    result=num1+num2
    print(f"The result is : {result}")                      

elif operation == "-":
    result=num1-num2
    print(f"The result is : {result}")  

elif operation == "*":
    result=num1*num2
    print(f"The result is : {result}")  

elif operation == "/":
    result = num1/num2
    print(f"The result is : {result}")
    if num2 == 0:
        print("Error,division by 0 is not possible")
elif operation != ("+" or "-"or"*"or "/" ):
    print("Invalid operation.Please choose a valid operation.")
else:
    while True:
        try:
            print(operation)
        except :
            print("Invalid operation.Please choose a valid operation.")