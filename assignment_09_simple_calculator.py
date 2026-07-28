# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Returns the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float | None:
    """Returns the quotient of two numbers, or None if dividing by zero."""
    if b == 0:
        return None
    return a / b


def modulus(a: float, b: float) -> float | None:
    """Returns the remainder of division, or None if dividing by zero."""
    if b == 0:
        return None
    return a % b


def power(a: float, b: float) -> float:
    """Returns a raised to the power of b."""
    return a**b


def format_num(val: float) -> str:
    """Formats floating-point values neatly (as int if whole, or rounded to 2 decimals)."""
    if val.is_integer():
        return str(int(val))
    return f"{val:.2f}"


def get_two_numbers() -> tuple[float, float] | None:
    """Helper function to safely get two numbers from the user."""
    try:
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numerical inputs.")
        return None


def display_menu() -> None:
    """Displays the calculator menu."""
    print("\n" + "=" * 28)
    print("      SIMPLE CALCULATOR")
    print("=" * 28)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def main() -> None:
    """Main program execution loop."""
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()

        if choice == "7":
            print("\nGoodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("Error: Invalid selection. Please enter a number from 1 to 7.")
            continue

        nums = get_two_numbers()
        if nums is None:
            continue

        num1, num2 = nums

        if choice == "1":
            res = add(num1, num2)
            print(f"Result: {format_num(num1)} + {format_num(num2)} = {format_num(res)}")

        elif choice == "2":
            res = subtract(num1, num2)
            print(f"Result: {format_num(num1)} - {format_num(num2)} = {format_num(res)}")

        elif choice == "3":
            res = multiply(num1, num2)
            print(f"Result: {format_num(num1)} * {format_num(num2)} = {format_num(res)}")

        elif choice == "4":
            res = divide(num1, num2)
            if res is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {format_num(num1)} / {format_num(num2)} = {res:.2f}")

        elif choice == "5":
            res = modulus(num1, num2)
            if res is None:
                print("Error: Cannot perform modulus by zero.")
            else:
                print(f"Result: {format_num(num1)} % {format_num(num2)} = {format_num(res)}")

        elif choice == "6":
            res = power(num1, num2)
            print(f"Result: {format_num(num1)} ** {format_num(num2)} = {format_num(res)}")


if __name__ == "__main__":
    main()