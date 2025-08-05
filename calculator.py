# Define a function to add two numbers
def add(x, y):
    return x + y

# Define a function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y

# Define a function to divide the first number by the second
def divide(x, y):
    if y == 0:
        # Check if the second number is zero to avoid division error
        return "Error: Cannot divide by zero"
    return x / y

# Main function to run the calculator
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")        # Option 1 for addition
    print("2. Subtract")   # Option 2 for subtraction
    print("3. Multiply")   # Option 3 for multiplication
    print("4. Divide")     # Option 4 for division

    # Ask user to choose an operation
    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ('1', '2', '3', '4'):
        try:
            # Take input numbers from user and convert them to float
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            # Handle the case where input is not a valid number
            print("Invalid input. Please enter numbers.")
            return

        # Perform the chosen operation and show the result
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        # If user enters an invalid choice
        print("Invalid choice")

# This line makes sure the calculator function runs only when this file is run directly
if __name__ == "__main__":
    calculator()
