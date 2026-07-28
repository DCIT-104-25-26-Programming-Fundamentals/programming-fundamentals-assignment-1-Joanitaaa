# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

import math


def generate_fibonacci(n: int) -> list[int]:
    """Generates a list containing the first N terms of the Fibonacci sequence."""
    if n <= 0:
        return []

    # First term edge case
    if n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence


def is_fibonacci_number(number: int) -> bool:
    """Checks whether a given non-negative integer is a Fibonacci number using an iterative loop."""
    if number < 0:
        return False

    a, b = 0, 1
    while a < number:
        a, b = b, a + b

    return a == number


if __name__ == "__main__":
    # --- PART A: Print First N Terms ---
    print("=========================================")
    print("PART A: Fibonacci Sequence Generator")
    print("=========================================")
    try:
        n_terms = int(input("How many terms? "))
        if n_terms <= 0:
            print("Error: Number of terms must be a positive integer.")
        else:
            fib_list = generate_fibonacci(n_terms)
            print("Fibonacci sequence:", " ".join(map(str, fib_list)))
    except ValueError:
        print("Error: Please enter a valid integer.")

    # --- PART B: Check if a Number Belongs to the Sequence ---
    print("\n=========================================")
    print("PART B: Fibonacci Number Checker")
    print("=========================================")
    try:
        check_num = int(input("Enter a number to check: "))

        if is_fibonacci_number(check_num):
            print(f"{check_num} is a Fibonacci number.")
        else:
            print(f"{check_num} is NOT a Fibonacci number.")
    except ValueError:
        print("Error: Please enter a valid integer.")