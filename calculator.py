import math

def scientific_calculator():
    print("Scientific Calculator")
    print("1. Square root\n2. Power")

    choice = input("Enter choice: ")

    if choice == '1':
        x = float(input("Enter number: "))
        print("Result:", math.sqrt(x))
    elif choice == '2':
        base = float(input("Enter base: "))
        exp = float(input("Enter exponent: "))
        print("Result:", math.pow(base, exp))
    else:
        print("Invalid choice")

scientific_calculator()
