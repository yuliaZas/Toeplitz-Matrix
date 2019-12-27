def matrixInit():
    """
        The function to initialize a matrix from the user.

        Returns:
            Matrix: A matrix
    """
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    matrix = []
    print("Enter the entries row wise:")
    for i in range(R):  # A for loop for row entries
        a = []
        for j in range(C):  # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)
    return matrix


def isToeplitz(matrix):
    """
        The function to check Toeplitz Matrix.

        Parameters:
            matrix (two-dimensional array): The two-dimensional array to check on.

        Returns:
            Boolean: A True if the matrix is toeplitz, else returns False
    """
    col = len(matrix[0])  # columns size //n
    row = len(matrix)  # rows size //m
    # indexes, i&ii for the rows, j&jj for the columns
    i = 0
    ii = 0
    j = 0
    jj = 0
    # first we check all the diagonals in the upper triangular matrix
    while j < col:
        val = matrix[i][j]
        # assign the next val in the diagonal
        ii = i + 1
        jj = j + 1
        while ii < row and jj < col:
            # if the val is'nt equal then we immediately brake the loop so we wont check the rest for nothing
            if val != matrix[ii][jj]:
                return False
            ii += 1
            jj += 1
        j += 1
    # now we check all the diagonals in the lower triangular matrix
    # except for the main diagonal to avoid double checking
    i = 1;  # we go a row down so we can skip checking the main diagonal
    j = 0;  # initializing the columns index
    while i < row:
        val = matrix[i][j]
        # assign the next val in the diagonal
        ii = i + 1
        jj = j + 1
        while ii < row and jj < col:
            # if the val is'nt equal then we immediately brake the loop so we wont check the rest for nothing
            if val != matrix[ii][jj]:
                return False
            ii += 1
            jj += 1
        i += 1
    return True


def main():
    matrix = matrixInit()
    is_toeplitz = isToeplitz(matrix)
    print(is_toeplitz)


if __name__ == "__main__":
    main()
