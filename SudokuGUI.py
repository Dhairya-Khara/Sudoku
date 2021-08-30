import os
import random
import sys
from copy import deepcopy

import pygame
import pygame.rect
import pygame_menu
from pygame_menu import Theme

from SudokuAbout import render_textrect
from SudokuSolver import solveBoardLoToHi, solveBoardHiToLo, keepCheckingValues

main_dir = os.path.split(os.path.abspath(__file__))[0]

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
font3 = pygame.font.SysFont("arial", 15)

windowSize = width, height = 500, 600
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Sudoku Visualizer by Dhairya Khara')

DARK_BLUE = (43, 50, 64)
ORANGE = (242, 153, 75)
LIGHT_GREY = (200, 200, 200)

BOX_COLOUR = (133, 150, 166)

dif = width / 9
x = 0
y = 0


def buttonToGenerateBoard(textColour):
    pygame.event.pump()
    text1 = font2.render("Generate Puzzle", True, textColour)
    screen.blit(text1, (20, 520))


def buttonToSolveBoard(textColour):
    text1 = font2.render("Solve Board", True, textColour)
    screen.blit(text1, (150, 520))


def buttonToMenu(textColour):
    text1 = font2.render("Menu", True, textColour)
    screen.blit(text1, (255, 520))


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
        pygame.draw.line(screen, DARK_BLUE, (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, DARK_BLUE, (i * dif, 0), (i * dif, 500), thick)


def draw(aBoard=None):
    if aBoard is None:
        aBoard = puzzle
    screen.fill(ORANGE)
    for i in range(9):
        for j in range(9):
            if aBoard[i][j] != 0:
                text1 = font1.render(str(aBoard[i][j]), 1, DARK_BLUE)
                screen.blit(text1, (j * dif + 20, i * dif + 20))

    # Draw lines horizontally and vertically to form grid
    drawOutlineLines()


def drawNumber(i, j, number):
    text1 = font1.render(str(number), True, DARK_BLUE)
    screen.blit(text1, (j * dif + 20, i * dif + 20))


def generateSolvedBoardGUI(aBoard=None):
    global puzzle
    puzzle = [
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

    if aBoard is None:
        aBoard = puzzle

    allowedNums = []
    previousChangedValues = []
    oldAllowedNums = []
    i = 0
    j = 0
    while i <= len(aBoard) - 1:
        while j <= len(aBoard[i]) - 1:
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
            oldAllowedNums[len(oldAllowedNums) - 1].remove(num)
            allowedNums = []

            pygame.event.pump()
            draw(aBoard)
            drawBoxWithGivenArguments(j, i)
            pygame.display.update()
            pygame.time.delay(50)

            j += 1
        j = 0
        i += 1
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
    generatePuzzleColour, solveBoardColour, menuColour = DARK_BLUE
    while run:
        pygame.event.pump()
        screen.fill(ORANGE)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 520 <= pos[1] <= 530:
                    if 20 <= pos[0] <= 120:
                        generatePuzzle()
                    elif 150 <= pos[0] <= 225:
                        solveBoardGUI()
                    elif 255 <= pos[0] <= 288:
                        menu.mainloop(screen)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    solveBoardGUI()
                if event.key == pygame.K_f:
                    generatePuzzle()
        if 520 <= pos[1] <= 530:
            if 20 <= pos[0] <= 120:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
                generatePuzzleColour = LIGHT_GREY
                solveBoardColour = DARK_BLUE
                menuColour = DARK_BLUE
            elif 150 <= pos[0] <= 225:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
                solveBoardColour = LIGHT_GREY
                generatePuzzleColour = DARK_BLUE
                menuColour = DARK_BLUE
            elif 255 <= pos[0] <= 288:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
                menuColour = LIGHT_GREY
                generatePuzzleColour = DARK_BLUE
                solveBoardColour = DARK_BLUE
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            generatePuzzleColour = DARK_BLUE
            solveBoardColour = DARK_BLUE
            menuColour = DARK_BLUE

        draw()

        buttonToGenerateBoard(generatePuzzleColour)
        buttonToSolveBoard(solveBoardColour)
        buttonToMenu(menuColour)

        pygame.display.update()


def drawAbout():
    my_rect = pygame.Rect(40, 20, 300, 600)
    textToDisplay = "This program gives a visualization of the backtracking algorithm and its application to solving " \
                    "sudoku puzzles. \n\nI have taken it one step further and used the same algorithm to generate " \
                    "unique sudoku puzzles. \n\nThe backtracking algorithm is quite straightforward to understand. " \
                    "The algorithm traverses a given matrix ( a 2 dimensional array which is our sudoku puzzle). If " \
                    "it detects a 0 (used to indicate a blank), it will try and insert a value between 1 and 9 in " \
                    "ascending order. Once a value is 'accepted' (a value is accepted when the same number is not in " \
                    "its corresponding row, column or square. Once the value is inserted, it will move on " \
                    "to the next element. The crux of this algorithm is to deal with the situation when not a single " \
                    "value (1-9) can be allotted to an index in the matrix. In that case, we go to the previous " \
                    "changed value and increment it by one. This process ensures that a solvable board will be " \
                    "solved. \n\nThis algorithm can also be used to generate unique puzzles. In order to generate " \
                    "puzzles, random values are inserted in an empty matrix until the matrix is full. The algorithm " \
                    "mentioned above ensures that the solved board follows the rules of sudoku. Once a unique solved " \
                    "board is prepared, random values are removed and the same algorithm is used to check if removing " \
                    "the random value still makes the board solvable or not. \n\nBy Dhairya Khara "
    text = render_textrect(
        textToDisplay,
        font3,
        my_rect,
        DARK_BLUE,
        ORANGE
        )
    if text:
        screen.blit(text, my_rect)


def about():
    while True:
        pygame.event.pump()
        screen.fill(ORANGE)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (520 <= pos[1] <= 540) and (400 <= pos[0] <= 470):
                    menu.mainloop(screen)
        if (520 <= pos[1] <= 540) and (400 <= pos[0] <= 470):
            text1 = font1.render("Menu", True, LIGHT_GREY)
            screen.blit(text1, (400, 520))
            pygame.mouse.set_cursor(pygame.cursors.tri_left)
        else:
            text1 = font1.render("Menu", True, DARK_BLUE)
            screen.blit(text1, (400, 520))
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        drawAbout()
        pygame.display.update()


menuTheme = Theme(background_color=ORANGE,
                  title_background_color=DARK_BLUE,
                  title_font_shadow=True,
                  widget_padding=25,
                  )

menu = pygame_menu.Menu('Sudoku Visualizer', width, height, theme=menuTheme)

menu.add.button('Start', startTheGame)
menu.add.button('About', about)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
