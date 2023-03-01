def row_reduce(matrix):
    """
    Converts an mxn matrix to its row reduced form using Gaussian elimination.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    pivot_row = 0
    
    for j in range(cols):
        # Find the pivot row for this column
        pivot_found = False
        for i in range(pivot_row, rows):
            if matrix[i][j] != 0:
                # Swap the rows if the pivot row is not the current row
                if i != pivot_row:
                    matrix[pivot_row], matrix[i] = matrix[i], matrix[pivot_row]
                pivot_found = True
                break
        
        if pivot_found:
            # Scale the pivot row so that the pivot element is 1
            pivot_element = matrix[pivot_row][j]
            matrix[pivot_row] = [elem / pivot_element for elem in matrix[pivot_row]]
            
            # Use the pivot row to eliminate the elements above and below it in the column
            for i in range(rows):
                if i != pivot_row:
                    factor = matrix[i][j] / matrix[pivot_row][j]
                    matrix[i] = [elem - factor * matrix[pivot_row][idx] for idx, elem in enumerate(matrix[i])]
            
            # Move to the next pivot row
            pivot_row += 1
        if pivot_row >= rows:
            break
    return(matrix)





