import echelonForm
def rank(mat):

    matrix=echelonForm.echelon_form(mat)

    """
    Calculates the rank of a matrix from its echelon form matrix.
    """
    rank = 0
    for row in matrix:
        if any(row):
            rank += 1
    return rank


def display(matrix):
    rnk=rank(matrix)
    print(rnk)

