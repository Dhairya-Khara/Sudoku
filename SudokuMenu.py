import pygame
import pygame_menu

pygame.init()
windowSize = width, height = 500, 500
screen = pygame.display.set_mode(windowSize)


def start_the_game():
    print("play")


menu = pygame_menu.Menu('Welcome', width, height)

menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)
