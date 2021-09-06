# Sudoku Visualizer
The primary purpose of this project was to deepen my understanding of the [Python](https://www.python.org/) programming language and the [backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking). 
The motivation of this project came from [Tech With Tim](https://www.youtube.com/c/TechWithTim)'s sudoku visualizer. Since he uses a recursive approach (the traditional way) to build his backtracking algorithm, I wanted to try something different and hence chose to use an iterative procedure.
Not only have I used this algorithm to solve sudoku boards, but also to generate unique sudoku puzzles. Both algorithms (generator and solver) have been implemented
using Python and visuzlied using [pygame](https://www.pygame.org/news). Another third party module, [pygame-menu](https://pygame-menu.readthedocs.io/en/4.1.3/), is used to organize the user interface.

## Getting Started
The easiest way to interact with the program is to run the included executable file (SudokuGUI.exe).  Do not move the location of the file. Instead run it from the root 
directory since it requires several included dependencies.

## Installation Guide
After cloning the repository, install all the required dependencies using pip.
```bash
pip install -r requirements.txt
```
The two python modules that are going to be installed will be pygame and pygame-menu.

## License
[MIT](https://choosealicense.com/licenses/mit/)

