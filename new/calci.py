def calculator():
    try:
        print("Simple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if choice == '1':
            print("Result:", num1 + num2)

        elif choice == '2':
            print("Result:", num1 - num2)

        elif choice == '3':
            print("Result:", num1 * num2)

        elif choice == '4':
            print("Result:", num1 / num2)

        elif choice == '5':
            print("Result:", num1 % num2)

        elif choice == '6':
            print("Result:", num1 ** num2)

        else:
            print("Invalid choice!")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        calculator()

    except ValueError:
        print("Error: Please enter valid numbers.")
        calculator()

calculator()
