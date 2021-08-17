from copy import deepcopy

board = [
    [0, 8, 0, 7, 0, 1, 0, 3, 0],
    [4, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 6, 0, 4, 1, 8],
    [7, 0, 0, 0, 0, 9, 0, 0, 0],
    [8, 0, 0, 6, 1, 0, 5, 0, 0],
    [0, 3, 5, 0, 0, 0, 0, 2, 9],
    [0, 6, 0, 4, 0, 7, 0, 9, 0],
    [1, 0, 0, 0, 0, 8, 0, 0, 4],
    [0, 2, 0, 0, 5, 0, 0, 7, 0]
]

board2Solutions = [
    [2, 9, 5, 7, 4, 3, 8, 6, 1],
    [4, 3, 1, 8, 6, 5, 9, 0, 0],
    [8, 7, 6, 1, 9, 2, 5, 4, 3],
    [3, 8, 7, 4, 5, 9, 2, 1, 6],
    [6, 1, 2, 3, 8, 7, 4, 9, 5],
    [5, 4, 9, 2, 1, 6, 7, 3, 8],
    [7, 6, 3, 5, 3, 4, 1, 8, 9],
    [9, 2, 8, 6, 7, 1, 3, 5, 4],
    [1, 5, 4, 9, 3, 8, 6, 0, 0]
]


def solveBoardLoToHi(aBoard):
    previousChangedValues = []
    i = 0
    j = 0
    while i <= len(aBoard) - 1:
        while j <= len(aBoard[i]) - 1:
            while aBoard[i][j] == 0:
                boardCopy = deepcopy(aBoard)
                trialValue = 1
                while keepCheckingValues(trialValue, boardCopy, i, j):
                    trialValue += 1
                    if trialValue >= 10:
                        aBoard[i][j] = 0
                        valuesRequiredToChange = previousChangedValues.pop()
                        i = valuesRequiredToChange[0]
                        j = valuesRequiredToChange[1]
                        aBoard[i][j] = 0
                        trialValue = valuesRequiredToChange[2]+1
                        boardCopy = deepcopy(aBoard)
                previousChangedValues.append([i, j, trialValue])
                aBoard[i][j] = trialValue
                break
            j += 1
        i += 1
        j = 0
    return aBoard


def solveBoardHiToLo(aBoard):
    counter = 0
    previousChangedValues = []
    i = 0
    j = 0
    while i <= len(aBoard) - 1:
        while j <= len(aBoard[i]) - 1:
            while aBoard[i][j] == 0:
                counter += 1
                boardCopy = deepcopy(aBoard)
                trialValue = 9
                while keepCheckingValues(trialValue, boardCopy, i, j):
                    trialValue -= 1
                    if trialValue <= 0:
                        aBoard[i][j] = 0
                        valuesRequiredToChange = previousChangedValues.pop()
                        i = valuesRequiredToChange[0]
                        j = valuesRequiredToChange[1]
                        aBoard[i][j] = 0
                        trialValue = valuesRequiredToChange[2]-1
                        boardCopy = deepcopy(aBoard)
                previousChangedValues.append([i, j, trialValue])
                aBoard[i][j] = trialValue
                break
            j += 1
        i += 1
        j = 0
    return aBoard


def keepCheckingValues(value, aBoard, aIndexI, aIndexJ):
    if value >= 10:
        return True
    statusOfValue = ""
    # check row
    while value in aBoard[aIndexI]:
        statusOfValue = "in row"
        return True
    # check column
    for indexI, i in enumerate(aBoard):
        if value == aBoard[indexI][aIndexJ]:
            statusOfValue = "in column"
            return True
    # check square
    startRow = (aIndexI // 3) * 3
    startColumn = (aIndexJ // 3) * 3
    for i in range(startRow, startRow + 3):
        for j in range(startColumn, startColumn + 3):
            if aBoard[i][j] == value:
                statusOfValue = "in square"
                return True
    statusOfValue = "value clear"
    return False


def printBoard(aBoard):
    for i in aBoard:
        print(i)

