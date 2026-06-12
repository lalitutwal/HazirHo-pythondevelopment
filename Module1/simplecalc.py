# simple calculator
# fuctions for add, multiply, divide and subtract
#
#


print("\n Simple python calculator \n")
print(
    """choose the option:
    \n 1. Addition        2. Subtraction
    \n 3. Multiplication  4. Division
    \n 5. remainder  6. exponent   \n"""
)
operator = int(input("enter operator (e.g. 1 for addition): "))

operand1 = eval(input("Enter the first operand: "))
operand2 = eval(input("Enter the second operand: "))


match operator:
    case 1:
        print(f"output is {operand1 + operand2}")

    case 2:
        print(f"output is {operand1 - operand2}")

    case 3:
        print(f"output is {operand1 * operand2}")

    case 4 if operand2 != 0:
        print(f"output is {operand1 / operand2}")

    case 5 if operand2 != 0:
        print(f"output is {operand1 % operand2}")

    case 6:
        print(f"output is {operand1**operand2}")

    case _:
        print("error: enter valid option")
