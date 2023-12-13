def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

while True:
    # Get user input for numbers and operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform calculation based on the chosen operation
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            continue

        # Display the result
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Ask if the user wants to perform another calculation
    another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
    if another_calculation != "yes":
        print("Exiting calculator. Goodbye!")
        break
