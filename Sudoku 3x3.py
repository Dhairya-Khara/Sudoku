from copy import deepcopy

board = [
    [0, 4, 0, 1],
    [3, 0, 4, 0],
    [1, 0, 0, 4],
    [0, 2, 1, 0]
]


# def solveBoard(aBoard):
#     previousChangedValue = 0
#     previousJValue = 0
#     for indexI, i in enumerate(aBoard):
#         for indexJ, j in enumerate(i):
#             while j == 0:
#                 boardCopy = deepcopy(aBoard)
#                 trialValue = 0
#                 while keepCheckingValues(trialValue, boardCopy, indexI, indexJ):
#                     trialValue += 1
#                 previousChangedValue = trialValue
#                 previousJValue = indexJ
#                 aBoard[indexI][indexJ] = trialValue
#                 break
#
#     return aBoard

def solveBoard(aBoard):
    counter = 0
    previousChangedValues = []
    valuesRequiredToChange = []
    i = 0
    j = 0
    while i <= len(aBoard) - 1:
        while j <= len(aBoard[i]) - 1:
            while aBoard[i][j] == 0:
                counter += 1
                boardCopy = deepcopy(aBoard)
                trialValue = 1
                while keepCheckingValues(trialValue, boardCopy, i, j):
                    trialValue += 1
                    if trialValue >= 5:
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
    startRow = (aIndexI // 2) * 2
    startColumn = (aIndexJ // 2) * 2
    for i in range(startRow, startRow + 1):
        for j in range(startColumn, startColumn + 1):
            if aBoard[i][j] == value:
                statusOfValue = "in square"
                return True
    statusOfValue = "value clear"
    return False


def printBoard(aBoard):
    for i in aBoard:
        print(i)


printBoard(solveBoard(board))
