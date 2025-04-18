def inverse_2x2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    determinant = a * d - b * c
    
    if determinant == 0:
        return "Matrix is singular and cannot be inverted."
    
    # Compute the inverse matrix
    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]
    
    return inverse

def get_matrix_input():
    matrix = []
    print("Enter the 2x2 matrix values row by row (values should be separated by spaces):")
    for i in range(2):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != 2:
            print("Invalid number of elements in row. Must be exactly 2 values.")
            return None
        matrix.append(row)
    
    return matrix

# Main program
matrix = get_matrix_input()
if matrix:
    inverse_matrix = inverse_2x2(matrix)
    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)
    print("\nInverse Matrix:")
    if isinstance(inverse_matrix, str):
        print(inverse_matrix)
    else:
        for row in inverse_matrix:
            print(row)