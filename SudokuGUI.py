import os
import random
import sys
from copy import deepcopy

import pygame
import pygame.rect
import pygame_menu
from pygame_menu import Theme

from SudokuAbout import drawAbout
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

pygame.init()  # pre-req for using pygame

# Load test fonts for future use
font1 = pygame.font.Font("Roboto-Medium.ttf", 24)
font2 = pygame.font.Font("Roboto-Medium.ttf", 12)


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
    """
    Renders text that acts as a button to generate puzzle
    :param textColour: colour of the text "Generate Puzzle" to be displayed
    :return: void
    """
    pygame.event.pump()
    text1 = font2.render("Generate Puzzle", True, textColour)
    screen.blit(text1, (20, 520))


def buttonToSolveBoard(textColour):
    """
    Renders text that acts as a button to solve the board
    :param textColour: colour of the text "Solve Board" to be displayed
    :return: void
    """
    text1 = font2.render("Solve Board", True, textColour)
    screen.blit(text1, (150, 520))


def buttonToMenu(textColour):
    """
    Renders text that acts as a button to go back to the menu
    :param textColour: colour of the text "Menu" to be displayed
    :return: void
    """
    text1 = font2.render("Menu", True, textColour)
    screen.blit(text1, (256, 520))


def drawBoxWithGivenArguments(aX, aY):
    """
    Draws two perpendicular outlines to mimic a box, used to highlight a specific cell on the drawn matrix
    :param aX: the x co-ordinate of the cell (row)
    :param aY: the y co-ordinate of the cell (col)
    :return: void
    """
    for i in range(2):
        pygame.draw.line(screen, BOX_COLOUR, (aX * dif - 3, (aY + i) * dif), (aX * dif + dif + 3, (aY + i) * dif), 7)
        pygame.draw.line(screen, BOX_COLOUR, ((aX + i) * dif, aY * dif), ((aX + i) * dif, aY * dif + dif), 7)


def drawOutlineLines():
    """
    Draws the grid outlines
    :return: void
    """
    # Draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, DARK_BLUE, (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, DARK_BLUE, (i * dif, 0), (i * dif, 500), thick)


def draw(aBoard=None):
    """
    Main draw method, handles all rendering
    :param aBoard: the matrix that is required to be drawn
    :return: void
    """
    if aBoard is None:
        aBoard = puzzle
    screen.fill(ORANGE)  # background colour
    for i in range(9):
        for j in range(9):
            if aBoard[i][j] != 0:  # since 0 is considered blank
                text1 = font1.render(str(aBoard[i][j]), True, DARK_BLUE)
                screen.blit(text1, (j * dif + 20, i * dif + 15))

    # Draw lines horizontally and vertically to form grid
    drawOutlineLines()


def drawNumber(row, col, number):
    """
    Renders an element at a particular spot
    :param row: the x co-ordinate of the cell the numbers wants to be rendered at
    :param col: the y co-ordinate of the cell the numbers wants to be rendered at
    :param number: the specific number to be drawn
    :return: void
    """
    text1 = font1.render(str(number), True, DARK_BLUE)
    screen.blit(text1, (col * dif + 20, row * dif + 20))


def generateSolvedBoardGUI(aBoard=None):
    """
    Generates and renders a unique and random solved sudoku board
    :param aBoard: Matrix used to hold the value of the generated board
    :return: The solved board (2d array)
    """
    global puzzle
    puzzle = [  # resetting the global board (puzzle) everytime a new board wants to be generated
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

            # pygame commands to visualize the generation
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
    """
    Removes numbers from the above generated board to create the puzzle
    :param aBoard: Matrix used to hold the value of the puzzle
    :return: Generated Puzzle (2d array)
    """
    if aBoard is None:
        aBoard = puzzle
    totalNumbersToRemove = 64  # maximum numbers possible to remove before a sudoku is unsolvable
    for i in range(0, totalNumbersToRemove):
        randomRow = random.randint(0, 8)
        randomCol = random.randint(0, 8)
        tempBoard = deepcopy(aBoard)
        oldValue = tempBoard[randomRow][randomCol]
        tempBoard[randomRow][randomCol] = 0
        solution1 = solveBoardLoToHi(tempBoard)
        solution2 = solveBoardHiToLo(tempBoard)

        # pygame commands to visualize the creation of the puzzle
        pygame.event.pump()
        draw()
        drawBoxWithGivenArguments(randomRow, randomCol)
        pygame.display.update()
        pygame.time.delay(50)

        while solution1 != solution2:  # ensures when one value is removed, only one possilbe solution is possible
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
    """
    Brings together the generation of the board and the creation of the puzzle (above two methods)
    :return: void
    """
    pygame.event.pump()
    generateSolvedBoardGUI()
    removeNumbersFromSolvedBoardGUI()


def solveBoardGUI(aBoard=None):
    """
    Solves and visualizes the backtracking algorithm used to solve sudoku puzzles
    :param aBoard: 2d array to solve
    :return: void
    """
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
    """
    Method with the main game loop
    :return: void
    """
    run = True
    generatePuzzleColour, solveBoardColour, menuColour = DARK_BLUE
    while run:
        pygame.event.pump()
        screen.fill(ORANGE)
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():  # handling user input
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 520 <= pos[1] <= 530:
                    if 20 <= pos[0] <= 107:
                        generatePuzzle()
                    elif 150 <= pos[0] <= 213:
                        solveBoardGUI()
                    elif 256 <= pos[0] <= 285:
                        menu.mainloop(screen)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    solveBoardGUI()
                if event.key == pygame.K_f:
                    generatePuzzle()
        if 520 <= pos[1] <= 530:  # highlighting buttons for visual clarity
            if 20 <= pos[0] <= 107:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
                generatePuzzleColour = LIGHT_GREY
                solveBoardColour = DARK_BLUE
                menuColour = DARK_BLUE
            elif 150 <= pos[0] <= 213:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
                solveBoardColour = LIGHT_GREY
                generatePuzzleColour = DARK_BLUE
                menuColour = DARK_BLUE
            elif 256 <= pos[0] <= 285:
                pygame.mouse.set_cursor(pygame.cursors.tri_left)
                menuColour = LIGHT_GREY
                generatePuzzleColour = DARK_BLUE
                solveBoardColour = DARK_BLUE
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                generatePuzzleColour = DARK_BLUE
                solveBoardColour = DARK_BLUE
                menuColour = DARK_BLUE
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


def about():
    """
    Method with the loop for the about page
    :return: void
    """
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
        drawAbout(screen)
        pygame.display.update()


# designing the menu using pygame_menu
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
