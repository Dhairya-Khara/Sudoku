import pygame

class TextRectException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message


def render_textrect(string, font, rect, text_color, background_color, justification=0):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Takes the following arguments:

    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rectstyle giving the size of the surface requested.
    text_color - a three-byte tuple of the rgb value of the
                 text color. ex (0, 0, 0) = BLACK
    background_color - a three-byte tuple of the rgb value of the surface.
    justification - 0 (default) left-justified
                    1 horizontally centered
                    2 right-justified

    Returns the following values:

    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    import pygame

    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line
                else:
                    final_lines.append(accumulated_line)
                    accumulated_line = word + " "
            final_lines.append(accumulated_line)
        else:
            final_lines.append(requested_line)

            # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size)
    surface.fill(background_color)

    accumulated_height = 0
    for line in final_lines:
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempsurface = font.render(line, 1, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException("Invalid justification argument: " + str(justification))
        accumulated_height += font.size(line)[1]

    return surface


def drawAbout(aScreen):
    DARK_BLUE = (43, 50, 64)
    ORANGE = (242, 153, 75)

    font3 = pygame.font.SysFont("arial", 15)
    my_rect = pygame.Rect(40, 20, 300, 600)
    textToDisplay = "This program gives a visualization of the backtracking algorithm and its application to solving " \
                    "sudoku puzzles. \n\nI have taken it one step further and used the same algorithm to generate " \
                    "unique sudoku puzzles. \n\nThe backtracking algorithm is quite straightforward to understand. " \
                    "The algorithm traverses a given matrix ( a 2 dimensional array which is our sudoku puzzle). If " \
                    "it detects a 0 (used to indicate a blank), it will try and insert a value between 1 and 9 in " \
                    "ascending order. Once a value is 'accepted' (a value is accepted when the same number is not in " \
                    "its corresponding row, column or square). Once the value is inserted, it will move on " \
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
        aScreen.blit(text, my_rect)

