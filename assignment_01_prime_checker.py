# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


import math


def is_prime(number: int) -> bool:
    """Checks whether a given integer is a prime number.

    A prime number is a whole number greater than 1 that has no positive
    divisors other than 1 and itself.
    """
    if number < 2:
        return False

    if number == 2:
        return True

    # Exclude all other even numbers
    if number % 2 == 0:
        return False

    # Check odd divisors up to the square root of the number
    limit = int(math.isqrt(number))
    for i in range(3, limit + 1, 2):
        if number % i == 0:
            return False

    return True


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number: "))

        if is_prime(user_input):
            print(f"{user_input} is a prime number.")
        else:
            print(f"{user_input} is NOT a prime number.")
    except ValueError:
        print("Please enter a valid integer.")