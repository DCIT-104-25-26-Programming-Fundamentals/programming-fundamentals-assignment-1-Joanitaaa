# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(number: int, max_multiplier: int = 12) -> None:
    """Prints the multiplication table for a given number from 1 up to max_multiplier."""
    print(f"\nMultiplication Table for {number}:")
    for i in range(1, max_multiplier + 1):
        product = number * i
        # String formatting keeps numbers neatly aligned
        print(f"  {number:<2} x {i:>2} = {product:>3}")


def print_tables_up_to_n(n: int) -> None:
    """Prints multiplication tables for every number from 1 up to N."""
    for current_num in range(1, n + 1):
        print_single_table(current_num)
        if current_num < n:
            print("---------------------------")


if __name__ == "__main__":
    # --- PART A: Single Table ---
    print("=========================================")
    print("PART A: Single Multiplication Table")
    print("=========================================")
    try:
        single_num = int(input("Enter a number: "))
        print_single_table(single_num)
    except ValueError:
        print("Error: Please enter a valid integer.")

    # --- PART B: Tables 1 to N ---
    print("\n=========================================")
    print("PART B: Multiplication Tables 1 to N")
    print("=========================================")
    try:
        n_input = int(input("Enter a number N: "))

        if n_input <= 0:
            print("Error: N must be a positive integer.")
        else:
            print_tables_up_to_n(n_input)

    except ValueError:
        print("Error: Please enter a valid integer.")