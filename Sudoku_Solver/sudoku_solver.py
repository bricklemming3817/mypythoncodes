import numpy as np  # importing numpy library


def solve(matrix):  # defining function to solve sudoku
    storage = []  # empty list to store parameters of randomly assigned values while solving
    counter, counter_ = 0, 0,  # two variables initialised to 0
    while np.count_nonzero(matrix) != 81:  # loop to iterate through the matrix until there are no zeros left
        for row in range(9):  # loop to iterate through the 9 rows of the matrix
            for col in range(9):  # loop to iterate though the 9 columns of the matrix
                if matrix[row, col] == 0:  # checking if the selected element is 0

                    num = [x for x in range(1, 10)]  # list in which natural number upto 9 is generated

                    n1 = (row + 3) % 3  # these six lines are used to select subgrid of the selected element
                    i0 = row - n1  # lower limit of row of the subgrid
                    i1 = row + (3 - n1)  # upper limit of the column of the subgrid

                    n2 = (col + 3) % 3
                    j0 = col - n2  # lower limit of column of the subgrid
                    j1 = col + (3 - n2)  # upper limit of column of the subgrid

                    sub = matrix[i0:i1, j0:j1]  # selecting the subgrid from the original matrix
                    for srow in range(3):  # iterating through the rows of the subgrid
                        for scol in range(3):  # iterating through the columns of the subgrid
                            if sub[srow, scol] != 0:  # checking if the element is non zero
                                try:  # if the element is non-zero it is removed from the generated 1-9 nos
                                    num.remove(sub[srow, scol])
                                except:  # try/except block is used to prevent errors while removing numbers
                                    pass

                    num = set(num)  # converting list to set for the simplicity of further procedures
                    mrow = set(matrix[row, :])  # converting the row and column of the selected element (contd.)
                    mcol = set(matrix[:, col])  # (contd.) and converting them to sets

                    num = num - mrow  # eliminating numbers present in row from num
                    num = num - mcol  # eliminating numbers present in columns from num
                    num = list(num)   # converting the set to a list

                    if len(num) == 1:  # if the number of elements in num is one
                        tnum = matrix[row, col]
                        matrix[row, col] = num[0] # that number is replaced inplace of 0
                        print('{} at position {},{} replaced to {}'.format(tnum, row, col, num[0]))  # printing summary

                    elif counter > counter_:  # this loop is used so that the coming block of codes runs (contd.)
                        if len(num) == 2:  # (contd.) of once in a single iteration of master while loop
                            matrix[row, col] = num[0]  # if the no. of element is 2 in num, random no. is substituted
                            storage.append((num[1], row, col, list(np.argwhere(matrix == 0))))  # the value(contd.)
                            counter_ = counter  # position of element and position of zeros are stored in the storage list
                            print('random number {} assigned at {},{}'.format(num[0], row, col))  # printing summary

                    if len(num) == 0:  # checking if the number of elements is zero in num
                        i = 1  # this block runs when the randomly assigned value above is wrong
                        for j in range(len(storage), 1, -1):  # loop which loops through previously stored data in storage
                            if storage[-j][0] in matrix[storage[-j][1], :] or storage[-j][0] in matrix[:,
                                                                                                storage[-j][2]]:
                                i += 0  # checks if the element is present in row or column of the matrix
                            else:
                                i += 1  # i is the index of the storage list
                        matrix[storage[-i][1], storage[-i][2]] = storage[-i][0]  # if the element is absent it is assigned

                        for trow, tcol in storage[-i][3]:  # reverting back all the changed to matrix until the (contd.)
                            matrix[trow, tcol] = 0  # (contd.) above substituion
                        print("random number at {},{} re-assigned to {}".format(storage[-i][1], storage[-i][2],
                                                                                storage[-i][0]))  # printing summary
                        del storage[-i:]  # deleting the substituted values and values after substitution from storage

        print('number of zeros: {} \n'.format(81 - np.count_nonzero(matrix)))  # printing the number of zeros after each iteration
        counter += 1
    return matrix  # returning the solved sudoku puzzel!!


b = np.array([[0, 0, 2, 0, 0, 9, 0, 0, 0],  # sample unsolved sudoku matrix where zeros are empty spaces
              [6, 9, 0, 0, 7, 0, 0, 3, 0],
              [0, 0, 0, 3, 5, 2, 6, 0, 0],
              [0, 0, 9, 0, 8, 5, 0, 0, 6],
              [0, 4, 0, 0, 0, 0, 0, 7, 0],
              [5, 0, 0, 4, 2, 0, 8, 0, 0],
              [0, 0, 1, 5, 9, 8, 0, 0, 0],
              [0, 2, 0, 0, 1, 0, 0, 5, 3],
              [0, 0, 0, 2, 0, 0, 1, 0, 0]])

a = np.array([[0, 7, 0, 0, 0, 0, 0, 0, 9],  # sample unsolved sudoku matrix where zeros are empty spaces
              [5, 1, 0, 4, 2, 0, 6, 0, 0],
              [0, 8, 0, 3, 0, 0, 7, 0, 0],
              [0, 0, 8, 0, 0, 1, 3, 7, 0],
              [0, 2, 3, 0, 8, 0, 0, 4, 0],
              [4, 0, 0, 9, 0, 0, 1, 0, 0],
              [9, 6, 2, 8, 0, 0, 0, 3, 0],
              [0, 0, 0, 0, 1, 0, 4, 0, 0],
              [7, 0, 0, 2, 0, 3, 0, 9, 6]])

print(solve(b))
