#function to get the numbers

def get_number(user_number):
    while True:
        try:
            number=float(input(user_number))
            return number
        except ValueError:
            print("Invalid number,Please try again")

#function to get operation

def get_operation():
    while True:
            op=input("Enter operation ; , + , - , * , /  : " )
            if op in ["+", "-", "*", "/"]:
                return op
            else:
                print("Invalid operation")

#function to calculate
 
def calculate(num1,num2,operation):
         if operation=="+":
             return num1+num2
        
         elif operation =="-":
                return num1-num2
         
         elif operation == "*":
             return num1*num2
         
         elif  operation == "/" :
            if num2 == 0:
                print("Error: division by zero")
            
         return num1/num2
         

def main():
    print("Welcome to Zeph's Calculator".center(50))
          
    num1=get_number("Enter your first number : ")
    num2=get_number("Enter your second number : ")

    operation=get_operation()

    result=calculate(num1,num2,operation)

    print(f"The result is : {result}")



main()




            
