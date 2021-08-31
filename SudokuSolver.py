from copy import deepcopy


def solveBoardLoToHi(aBoard):
    """returns a solved board. This algorithm uses backtracking and values are inserted in ascending order (from 1-9)

    :param aBoard: 2d array, 0 is considered a blank
    :return: returns the solved board
    """

    previousChangedValues = []  # used to keep track of inserted value and its
    # location in the matrix. Each element is an array that holds information on the changed value.
    # The order of the inserted array is its row, column and the actual value.
    row = 0
    col = 0
    while row <= len(aBoard) - 1:
        while col <= len(aBoard[row]) - 1:
            while aBoard[row][col] == 0:
                boardCopy = deepcopy(aBoard)
                trialValue = 1
                while keepCheckingValues(trialValue, boardCopy, row, col):
                    trialValue += 1
                    if trialValue >= 10:
                        aBoard[row][col] = 0
                        valuesRequiredToChange = previousChangedValues.pop()
                        row = valuesRequiredToChange[0]
                        col = valuesRequiredToChange[1]
                        aBoard[row][col] = 0
                        trialValue = valuesRequiredToChange[2] + 1
                        boardCopy = deepcopy(aBoard)
                previousChangedValues.append([row, col, trialValue])
                aBoard[row][col] = trialValue
                break
            col += 1
        row += 1
        col = 0
    return aBoard


def solveBoardHiToLo(aBoard):
    """returns a solved board. This algorithm uses backtracking and values are inserted in descending order (from 9-1)

    :param aBoard: 2d array, 0 is considered a blank
    :return: returns the solved board
    """
    previousChangedValues = []  # used to keep track of inserted value and its
    # location in the matrix. Each element is an array that holds information on the changed value.
    # The order of the inserted array is its row, column and the actual value.
    row = 0
    col = 0
    while row <= len(aBoard) - 1:
        while col <= len(aBoard[row]) - 1:
            while aBoard[row][col] == 0:
                boardCopy = deepcopy(aBoard)
                trialValue = 9
                while keepCheckingValues(trialValue, boardCopy, row, col):
                    trialValue -= 1
                    if trialValue <= 0:
                        aBoard[row][col] = 0
                        valuesRequiredToChange = previousChangedValues.pop()
                        row = valuesRequiredToChange[0]
                        col = valuesRequiredToChange[1]
                        aBoard[row][col] = 0
                        trialValue = valuesRequiredToChange[2] - 1
                        boardCopy = deepcopy(aBoard)
                previousChangedValues.append([row, col, trialValue])
                aBoard[row][col] = trialValue
                break
            col += 1
        row += 1
        col = 0
    return aBoard


def keepCheckingValues(value, aBoard, aRow, aCol):
    """ Used to check the validity of a value. Checks the value's row, col and respective square as per the rules of sudoku.

    :param value: Value to check
    :param aBoard: The matrix to check the value in (2d array)
    :param aRow: Row to check the value on
    :param aCol: Col to check the value on
    :return: True if value is not valid (exists in row, col or square), False if value is valid
    """
    if value >= 10:
        return True
    # check row
    while value in aBoard[aRow]:
        return True
    # check column
    for indexI, i in enumerate(aBoard):
        if value == aBoard[indexI][aCol]:
            return True
    # check square
    startRow = (aRow // 3) * 3
    startColumn = (aCol // 3) * 3
    for i in range(startRow, startRow + 3):
        for j in range(startColumn, startColumn + 3):
            if aBoard[i][j] == value:
                return True
    return False


def printBoard(aBoard):
    """
    Used to output a 2d array, used for debugging
    :param aBoard: 2d array
    :return: void
    """
    for i in aBoard:
        print(i)
