from SudokuSolver import printBoard, solveBoardLoToHi, solveBoardHiToLo, keepCheckingValues
from copy import deepcopy
import random

emptyBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


# def generatePuzzle(aBoard):
#     allowedNums = []
#     previousChangedValues = []
#     oldAllowedNums = []
#     for indexI, i in enumerate(emptyBoard):
#         for indexJ, j in enumerate(i):
#             for k in range(1, 10):
#                 if not keepCheckingValues(k, aBoard, indexI, indexJ):
#                     allowedNums.append(k)
#             if allowedNums == []:
#                 #undo
#
#             try:
#                 oldAllowedNums = deepcopy(allowedNums)
#                 num = allowedNums[random.randint(0, len(allowedNums) - 1)]
#                 aBoard[indexI][indexJ] = num
#                 previousChangedValues.append([indexI, indexJ, num])
#                 oldAllowedNums.remove(num)
#                 allowedNums = []
#             except:
#                 print(allowedNums)
#     return aBoard

def generateSolvedBoard(aBoard):
    allowedNums = []
    previousChangedValues = []
    oldAllowedNums = []
    i = 0
    j = 0
    while i <= len(aBoard)-1:
        while j <= len(aBoard[i])-1:
            for k in range(1, 10):
                if not keepCheckingValues(k, aBoard, i, j):
                    allowedNums.append(k)
            while not allowedNums:
                valuesRequiredToChange = previousChangedValues.pop()
                i = valuesRequiredToChange[0]
                j = valuesRequiredToChange[1]
                aBoard[i][j] = 0
                popOldAllowedNums = oldAllowedNums.pop()
                allowedNums = popOldAllowedNums

            oldAllowedNums.append(allowedNums)
            num = allowedNums[random.randint(0, len(allowedNums) - 1)]
            aBoard[i][j] = num
            previousChangedValues.append([i, j, num])
            oldAllowedNums[len(oldAllowedNums)-1].remove(num)
            allowedNums = []

            j += 1
        j = 0
        i += 1
    return aBoard


def generatePuzzle(aBoard):
    totalNumbersToRemove = random.randint(40, 64)
    for i in range (0, totalNumbersToRemove):
        randomRow = random.randint(0, 8)
        randomCol = random.randint(0, 8)
        tempBoard = deepcopy(aBoard)
        oldValue = tempBoard[randomRow][randomCol]
        tempBoard[randomRow][randomCol] = 0
        solution1 = solveBoardLoToHi(tempBoard)
        solution2 = solveBoardHiToLo(tempBoard)
        while solution1 != solution2:
            tempBoard[randomRow][randomCol] = oldValue
            randomRow = random.randint(0, 8)
            randomCol = random.randint(0, 8)
            tempBoard = deepcopy(aBoard)
            tempBoard[randomRow][randomCol] = 0
            solution1 = solveBoardLoToHi(tempBoard)
            solution2 = solveBoardHiToLo(tempBoard)
        aBoard[randomRow][randomCol] = 0
    return aBoard




printBoard(generatePuzzle(generateSolvedBoard(emptyBoard)))
print(" ")
# printBoard(generateSolvedBoard(emptyBoard))
printBoard(solveBoardLoToHi(emptyBoard))
print(" ")
printBoard(solveBoardHiToLo(emptyBoard))





