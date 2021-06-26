import numpy as np  # importing numpy


def solve(matrix):  # defining function to solve sudoku puzzle
    while np.count_nonzero(matrix) != 81:  # loop that runs the process until there are no zeroes in the matrix
        for row in range(9):  # for loop to iterate through the rows
            for col in range(9):  # for loop to iterate through columns
                if matrix[row, col] == 0:  # checking if the iterated element is zero

                    num = [x for x in range(1, 10)]  # generating natural nums from 1 to 9 to fill in empty space

                    n1 = (row + 3) % 3  # these six lines of codes are used to select the nine sub-matrices individually
                    i0 = row - n1  # lower bound of row of the sub-matrix
                    i1 = row + (3 - n1)  # upper bound of row of the sub-matrix

                    n2 = (col + 3) % 3
                    j0 = col - n2  # lower bound of column of the sub-matrix
                    j1 = col + (3 - n2)  # upper bound of column of the sub-matrix

                    sub = matrix[i0:i1, j0:j1]  # selecting the sub-matrix and assigning to variable 'sub'
                    for srow in range(3):  # for loop to iterate through the rows of the sub-matrix
                        for scol in range(3):  # for loop to iterate through the columns of the sub-matrix
                            if sub[srow, scol] != 0:  # checking if the iterated element of the sub-matrix is zero
                                num.remove(sub[srow, scol])  # if the element is non-zero it is removed from list 'num'

                    num = set(num)  # converting list num to a set. This is done to easily eliminate elements
                    mrow = set(matrix[row, :])  # converting the row associated to the selected element to set
                    mcol = set(matrix[:, col])  # converting the column associated to the selected element to set

                    num = num - mrow  # eliminating numbers present in row from num
                    num = num - mcol  # eliminating numbers present in column from num
                    num = list(num)  # converting set num to a list

                    if len(num) == 1:  # checking if all the size of num is 1. If it is not that means there are (cont.)
                        matrix[row, col] = num[0]  # (cont.)multiple values that can be assigned. Num assigned otherwise
                    else:
                        pass  # assigning is skipped and will be carried out in future iterations
    return matrix  # once all the zeros are replaced the final matrix is returned


a = np.array([[0, 7, 0, 0, 0, 0, 0, 0, 9],  # incomplete sudoku puzzle (matrix) to be solved
              [5, 1, 0, 4, 2, 0, 6, 0, 0],
              [0, 8, 0, 3, 0, 0, 7, 0, 0],
              [0, 0, 8, 0, 0, 1, 3, 7, 0],
              [0, 2, 3, 0, 8, 0, 0, 4, 0],
              [4, 0, 0, 9, 0, 0, 1, 0, 0],
              [9, 6, 2, 8, 0, 0, 0, 3, 0],
              [0, 0, 0, 0, 1, 0, 4, 0, 0],
              [7, 0, 0, 2, 0, 3, 0, 9, 6]])

print(solve(a))  # calling the function to solve the puzzle a and printing the result
