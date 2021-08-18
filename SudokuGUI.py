import os, pygame
import sys
from SudokuGenerator import generatePuzzle, generateSolvedBoard
from SudokuSolver import printBoard

# get random sudoku board
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

puzzle = generatePuzzle(generateSolvedBoard(emptyBoard))
printBoard(puzzle)

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


def draw(grid):

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                text1 = font1.render(str(grid[i][j]), 1, BLACK)
                screen.blit(text1, (i * dif + 20, j * dif + 20))

    # Draw lines horizontally and vertically to form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


run = True
drawRedBox = False
while run:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            get_cord(pos)
            drawRedBox = True

    draw(puzzle)
    if drawRedBox:
        draw_box()
    pygame.display.update()
