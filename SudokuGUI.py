import os, pygame
import sys
import time
import random
from copy import deepcopy
from SudokuGenerator import keepCheckingValues
from SudokuSolver import solveBoardLoToHi, solveBoardHiToLo

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


puzzle = emptyBoard

pygame.init()

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

windowSize = width, height = 500, 500
screen = pygame.display.set_mode(windowSize)

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
dif = width / 9
x = 0
y = 0


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


def drawBoxWithGivenArguments(aX, aY):
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (aX * dif - 3, (aY + i) * dif), (aX * dif + dif + 3, (aY + i) * dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ((aX + i) * dif, aY * dif), ((aX + i) * dif, aY * dif + dif), 7)


def drawOutlineLines():
    # Draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


def draw(aBoard=puzzle):
    screen.fill(WHITE)
    for i in range(9):
        for j in range(9):
            if aBoard[i][j] != 0:
                text1 = font1.render(str(aBoard[i][j]), 1, BLACK)
                screen.blit(text1, (j * dif + 20, i * dif + 20))

    # Draw lines horizontally and vertically to form grid
    drawOutlineLines()


def drawNumber(i, j, number):
    text1 = font1.render(str(number), 1, BLACK)
    screen.blit(text1, (j * dif + 20, i * dif + 20))


def generateSolvedBoardGUI(aBoard=puzzle):
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

            draw(aBoard)
            drawBoxWithGivenArguments(j, i)
            pygame.display.update()
            pygame.time.delay(50)

            j += 1
        j = 0
        i += 1
    # removeNumbersFromSolvedBoardGUI()
    return aBoard


def removeNumbersFromSolvedBoardGUI(aBoard=puzzle):
    totalNumbersToRemove = 64
    for i in range(0, totalNumbersToRemove):
        randomRow = random.randint(0, 8)
        randomCol = random.randint(0, 8)
        tempBoard = deepcopy(aBoard)
        oldValue = tempBoard[randomRow][randomCol]
        tempBoard[randomRow][randomCol] = 0
        solution1 = solveBoardLoToHi(tempBoard)
        solution2 = solveBoardHiToLo(tempBoard)

        draw()
        drawBoxWithGivenArguments(randomRow, randomCol)
        pygame.display.update()
        pygame.time.delay(50)

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


def generatePuzzle():
    generateSolvedBoardGUI()
    removeNumbersFromSolvedBoardGUI()


def solveBoardGUI(aBoard=puzzle):
    previousChangedValues = []
    i = 0
    j = 0
    while i <= len(aBoard) - 1:
        while j <= len(aBoard[i]) - 1:
            draw()
            drawBoxWithGivenArguments(j, i)
            pygame.display.update()
            pygame.time.delay(50)
            while aBoard[i][j] == 0:
                boardCopy = deepcopy(aBoard)
                trialValue = 1
                drawNumber(i, j, trialValue)
                while keepCheckingValues(trialValue, boardCopy, i, j):
                    trialValue += 1
                    drawNumber(i, j, trialValue)
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


run = True
drawRedBox = False
while run:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            get_cord(pos)
            drawRedBox = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                solveBoardGUI()
            if event.key == pygame.K_f:
                generatePuzzle()

    draw()
    if drawRedBox:
        draw_box()
    pygame.display.update()
