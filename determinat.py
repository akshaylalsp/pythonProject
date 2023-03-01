def determinant(matrix):
    """
    Calculates the determinant of a matrix using a recursive algorithm.
    """

    
    # Base case: 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]
    
    # Base case: 2x2 matrix
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    
    det = 0
    
    # Iterate over the first row of the matrix
    for j in range(len(matrix)):
        # Calculate the submatrix by removing the first row and j-th column
        submatrix = [[matrix[i][k] for k in range(len(matrix)) if k != j] for i in range(1, len(matrix))]
        
        # Add or subtract the product of the first element and the determinant of the submatrix
        det += (-1)**j * matrix[0][j] * determinant(submatrix)
    
    return det


def display(matrix):
    if(len(matrix)==len(matrix[0])):
        det=determinant(matrix)
        print(det)
    else :
        print("it should be square matrix!!")



