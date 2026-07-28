# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# def print_matrix(matrix: list[list[float]]) -> None:
    """Prints a 2D list in a neatly aligned grid format."""
    for row in matrix:
        formatted_row = [
            f"{int(val):>4}" if val.is_integer() else f"{val:>6.2f}"
            for val in row
        ]
        print(" ".join(formatted_row))


def get_matrix_input(rows: int, cols: int, name: str = "Matrix") -> list[list[float]]:
    """Helper function to read a matrix from user input row by row."""
    print(f"\n--- Enter values for {name} ({rows}x{cols}) ---")
    matrix = []
    for i in range(1, rows + 1):
        while True:
            try:
                line = input(f"Enter row {i}: ").strip().split()
                if len(line) != cols:
                    print(f"Error: Row must contain exactly {cols} numbers separated by spaces.")
                    continue
                row = [float(x) for x in line]
                matrix.append(row)
                break
            except ValueError:
                print("Error: Invalid entry. Please enter numbers separated by spaces.")
    return matrix


# =============================================================================
# PART A — Transpose
# =============================================================================
def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """Computes the transpose of an M x N matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    # Create empty N x M matrix initialized with zeros
    transposed = [[0.0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


# =============================================================================
# PART B — Addition
# =============================================================================
def add_matrices(
    matrix_a: list[list[float]], matrix_b: list[list[float]]
) -> list[list[float]] | None:
    """Adds two M x N matrices element-wise using nested loops."""
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    if rows_a != rows_b or cols_a != cols_b:
        return None

    result = [[0.0 for _ in range(cols_a)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_a):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


# =============================================================================
# PART C — Multiplication
# =============================================================================
def multiply_matrices(
    matrix_a: list[list[float]], matrix_b: list[list[float]]
) -> list[list[float]] | None:
    """Multiplies matrix A (M x N) by matrix B (N x P) using nested loops."""
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    
    if cols_a != rows_b:
        return None

    result = [[0.0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            dot_product = 0.0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = dot_product

    return result


# =============================================================================
# MAIN INTERACTIVE MENU
# =============================================================================
def main():
    while True:
        print("\n" + "=" * 40)
        print("     MATRIX OPERATIONS MENU")
        print("=" * 40)
        print("1. Transpose a Matrix (Part A)")
        print("2. Add Two Matrices (Part B)")
        print("3. Multiply Two Matrices (Part C)")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            try:
                m = int(input("\nEnter number of rows: "))
                n = int(input("Enter number of columns: "))
                if m <= 0 or n <= 0:
                    print("Error: Dimensions must be positive integers.")
                    continue
                
                mat = get_matrix_input(m, n, "Original Matrix")
                print("\nOriginal Matrix:")
                print_matrix(mat)

                transposed = transpose_matrix(mat)
                print("\nTransposed Matrix:")
                print_matrix(transposed)
            except ValueError:
                print("Error: Dimensions must be valid integers.")

        elif choice == "2":
            try:
                m = int(input("\nEnter rows for both matrices: "))
                n = int(input("Enter columns for both matrices: "))
                if m <= 0 or n <= 0:
                    print("Error: Dimensions must be positive integers.")
                    continue

                mat_a = get_matrix_input(m, n, "Matrix A")
                mat_b = get_matrix_input(m, n, "Matrix B")

                result = add_matrices(mat_a, mat_b)
                if result:
                    print("\nResult (Matrix A + Matrix B):")
                    print_matrix(result)
                else:
                    print("Error: Matrices must have identical dimensions for addition.")
            except ValueError:
                print("Error: Dimensions must be valid integers.")

        elif choice == "3":
            try:
                m_a = int(input("\nEnter rows for Matrix A (M): "))
                n_a = int(input("Enter columns for Matrix A (N): "))
                n_b = int(input("Enter rows for Matrix B (must equal N): "))
                p_b = int(input("Enter columns for Matrix B (P): "))

                if n_a != n_b:
                    print("\nError: Cannot multiply! Columns of Matrix A must equal Rows of Matrix B.")
                    continue
                if m_a <= 0 or n_a <= 0 or p_b <= 0:
                    print("Error: Dimensions must be positive integers.")
                    continue

                mat_a = get_matrix_input(m_a, n_a, "Matrix A")
                mat_b = get_matrix_input(n_b, p_b, "Matrix B")

                result = multiply_matrices(mat_a, mat_b)
                if result:
                    print(f"\nResult (Matrix A × Matrix B) [{m_a}x{p_b}]:")
                    print_matrix(result)
            except ValueError:
                print("Error: Dimensions must be valid integers.")

        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()