from copy import deepcopy



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
                        trialValue = valuesRequiredToChange[2] + 1
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
                        trialValue = valuesRequiredToChange[2] - 1
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
    # check row
    while value in aBoard[aIndexI]:
        return True
    # check column
    for indexI, i in enumerate(aBoard):
        if value == aBoard[indexI][aIndexJ]:
            return True
    # check square
    startRow = (aIndexI // 3) * 3
    startColumn = (aIndexJ // 3) * 3
    for i in range(startRow, startRow + 3):
        for j in range(startColumn, startColumn + 3):
            if aBoard[i][j] == value:
                return True
    return False


def printBoard(aBoard):
    for i in aBoard:
        print(i)

