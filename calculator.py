def programmer_calculator():
    print("Programmer Calculator")
    print("1. Binary to Decimal\n2. Decimal to Binary")

    choice = input("Enter choice: ")

    if choice == '1':
        b = input("Enter binary number: ")
        print("Decimal:", int(b, 2))
    elif choice == '2':
        d = int(input("Enter decimal number: "))
        print("Binary:", bin(d)[2:])
    else:
        print("Invalid choice")

programmer_calculator()
