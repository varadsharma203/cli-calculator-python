# --- 1. OPERATION FUNCTIONS ---
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

def power(n1, n2):
    """Calculates n1 raised to the power of n2 (n1 ** n2)"""
    return n1 ** n2

def square_root(n):
    """Calculates the square root of n using the ** operator (n ** 0.5)"""
    if n < 0:
        # Note: While n ** 0.5 can return a complex number for negatives,
        # we return an error string here for a simple calculator application.
        return "Error: Cannot calculate the square root of a negative number"
    return n ** 0.5 # <--- The key change: Using the built-in exponentiation operator

def modulo(n1, n2):
    """Calculates the remainder of n1 divided by n2 (n1 % n2)"""
    if n2 == 0:
        return "Error: Cannot modulo by zero"
    return n1 % n2

# --- 2. MAIN CALCULATOR LOOP ---
def calculator():
    print("Welcome to the CLI Calculator! 💻")

    while True:
        # Display the menu of available operations
        print("\n" + "=" * 30)
        print("Please select an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Square Root (√) - Takes one number")
        print("7. Modulo (%)")
        print("8. Exit")
        print("=" * 30)

        choice = input("Enter choice (1-8): ")

        # Check for exit command
        if choice == '8':
            print("Exiting calculator.")
            break

        # Operations that require TWO numbers (Choices 1, 2, 3, 4, 5, 7)
        if choice in ('1', '2', '3', '4', '5', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("⚠️ Invalid input. Please enter valid numerical values.")
                continue

            # Perform the chosen operation
            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
            elif choice == '7':
                result = modulo(num1, num2)

        # Operation that requires ONE number (Choice 6: Square Root)
        elif choice == '6':
            try:
                num = float(input("Enter the number: "))
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid numerical value.")
                continue
            
            result = square_root(num)

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 8.")
            continue
            
        # Display the result
        print(f"\n✨ Result: {result}\n")


# --- 3. SCRIPT EXECUTION ---
if __name__ == "__main__":
    calculator()
