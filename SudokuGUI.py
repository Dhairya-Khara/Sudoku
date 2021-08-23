import pygame
import sys
import pygame_menu
import random
from copy import deepcopy
from SudokuSolver import solveBoardLoToHi, solveBoardHiToLo, keepCheckingValues

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

windowSize = width, height = 500, 600
screen = pygame.display.set_mode(windowSize)

BLACK = (43, 50, 64)
WHITE = (242, 153, 75)
BOX_COLOUR = (133, 150, 166)

dif = width / 9
x = 0
y = 0


# Display instruction for the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, (0, 0, 0))
    screen.blit(text1, (20, 520))
    screen.blit(text2, (20, 540))


def buttonToGenerateBoard():
    pygame.event.pump()
    text1 = font2.render("Generate Puzzle", 1, BLACK)
    screen.blit(text1, (20, 520))


def buttonToSolveBoard():
    text1 = font2.render("Solve Board", 1, BLACK)
    screen.blit(text1, (150, 520))


def buttonToMenu():
    text1 = font2.render("Menu", 1, BLACK)
    screen.blit(text1, (150, 520))


def get_cord(pos):
    global x
    x = pos[0] // dif
    global y
    y = pos[1] // dif


def draw_box():
    for i in range(2):
        pygame.draw.line(screen, BOX_COLOUR, (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, BOX_COLOUR, ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


def drawBoxWithGivenArguments(aX, aY):
    for i in range(2):
        pygame.draw.line(screen, BOX_COLOUR, (aX * dif - 3, (aY + i) * dif), (aX * dif + dif + 3, (aY + i) * dif), 7)
        pygame.draw.line(screen, BOX_COLOUR, ((aX + i) * dif, aY * dif), ((aX + i) * dif, aY * dif + dif), 7)


def drawOutlineLines():
    # Draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, BLACK, (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, BLACK, (i * dif, 0), (i * dif, 500), thick)


def draw(aBoard=None):
    if aBoard is None:
        aBoard = puzzle
    screen.fill(WHITE)
    for i in range(9):
        for j in range(9):
            if aBoard[i][j] != 0:
                text1 = font1.render(str(aBoard[i][j]), 1, BLACK)
                screen.blit(text1, (j * dif + 20, i * dif + 20))

    # Draw lines horizontally and vertically to form grid
    drawOutlineLines()
    buttonToGenerateBoard()
    buttonToSolveBoard()


def drawNumber(i, j, number):
    text1 = font1.render(str(number), 1, BLACK)
    screen.blit(text1, (j * dif + 20, i * dif + 20))


def generateSolvedBoardGUI(aBoard=None):
    if aBoard is None:
        aBoard = puzzle
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

            pygame.event.pump()
            draw(aBoard)
            drawBoxWithGivenArguments(j, i)
            pygame.display.update()
            pygame.time.delay(50)

            j += 1
        j = 0
        i += 1
    # removeNumbersFromSolvedBoardGUI()
    return aBoard


def removeNumbersFromSolvedBoardGUI(aBoard=None):
    if aBoard is None:
        aBoard = puzzle
    totalNumbersToRemove = 64
    for i in range(0, totalNumbersToRemove):
        randomRow = random.randint(0, 8)
        randomCol = random.randint(0, 8)
        tempBoard = deepcopy(aBoard)
        oldValue = tempBoard[randomRow][randomCol]
        tempBoard[randomRow][randomCol] = 0
        solution1 = solveBoardLoToHi(tempBoard)
        solution2 = solveBoardHiToLo(tempBoard)

        pygame.event.pump()
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
    pygame.event.pump()
    generateSolvedBoardGUI()
    removeNumbersFromSolvedBoardGUI()


def solveBoardGUI(aBoard=None):
    if aBoard is None:
        aBoard = puzzle
    previousChangedValues = []
    i = 0
    j = 0
    while i <= len(aBoard) - 1:
        while j <= len(aBoard[i]) - 1:
            pygame.event.pump()
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


def startTheGame():
    run = True
    drawRedBox = False
    while run:
        pygame.event.pump()
        screen.fill(WHITE)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if 520 <= pos[1] <= 530:
                    if 20 <= pos[0] <= 120:
                        generatePuzzle()
                    elif 150 <= pos[0] <= 225:
                        solveBoardGUI()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    solveBoardGUI()
                if event.key == pygame.K_f:
                    generatePuzzle()
        if 520 <= pos[1] <= 530:
            if 20 <= pos[0] <= 120:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
            elif 150 <= pos[0] <= 225:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        draw()
        pygame.display.update()


menu = pygame_menu.Menu('Welcome', width, height)

menu.add.button('Play', startTheGame)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
