def get_number(user_number):
    while True:
        try:
            number = float(input(user_number))
            return number

        except ValueError:
            print("Invalid number. Please try again.")


def get_operation():
    while True:
        op = input("Enter operation (+, -, *, /): ")

        if op in ["+", "-", "*", "/"]:
            return op

        print("Invalid operation")