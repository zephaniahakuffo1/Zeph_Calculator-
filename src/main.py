from input_handler import get_number, get_operation
from calculator import calculate


def main():
    while True:

        print("Welcome to Zeph's Calculator".center(50))

        num1 = get_number("Enter your first number: ")
        num2 = get_number("Enter your second number: ")

        operation = get_operation()

        result = calculate(num1, num2, operation)

        print(f"The result is: {result}")

        continue_calculation = input(
            "Do you want another calculation? (yes/no): "
        ).strip().lower()

        if continue_calculation != "yes":
            print("Thank you for using Zeph's Calculator.")
            break


if __name__ == "__main__":
    main()