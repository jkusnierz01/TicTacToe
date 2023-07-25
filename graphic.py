import pygame
import sys
from TicTacToeLogic import *

WIDTH = 600
HEIGHT = 700
dt = 0
x = 145
y = 220


def approx_cords(gameboard_cords_dict: dict, move_cords: tuple) -> tuple:
    x_cord_list = list()
    y_cord_list = list()
    gameboard_cords_list = list(gameboard_cords_dict.values())
    for x in gameboard_cords_list:
        x_cord_list.append(x[0])
        y_cord_list.append(x[1])
    x_cord = min(x_cord_list, key=lambda x:abs(x+35-move_cords[0]))
    y_cord = min(y_cord_list, key=lambda x:abs(x+35-move_cords[1]))
    tup = (x_cord,y_cord)
    return tup




game_cords_match = {
    (0, 0): (60, 135),
    (0, 1): (160, 135),
    (0, 2): (260, 135),
    (0, 3): (360, 135),
    (0, 4): (460, 135),
    (1, 0): (60, 235),
    (1, 1): (160, 235),
    (1, 2): (260, 235),
    (1, 3): (360, 235),
    (1, 4): (460, 235),
    (2, 0): (60, 335),
    (2, 1): (160, 335),
    (2, 2): (260, 335),
    (2, 3): (360, 335),
    (2, 4): (460, 335),
    (3, 0): (60, 435),
    (3, 1): (160, 435),
    (3, 2): (260, 435),
    (3, 3): (360, 435),
    (3, 4): (460, 435),
    (4, 0): (60, 535),
    (4, 1): (160, 535),
    (4, 2): (260, 535),
    (4, 3): (360, 535),
    (4, 4): (460, 535)
}
game_cords_match_reverse = {value: key for key, value in game_cords_match.items()}


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
background = pygame.image.load("grass.jpeg")
x_mark = pygame.image.load("x_mark.jpg")
o_mark = pygame.image.load("o_mark.jpg")

def init_board(x: int, y: int):
    for z in range(4):
        z = z * 100
        pygame.draw.aaline(background, "black", (x + z, 120), (x + z, HEIGHT - 80))
        pygame.draw.aaline(background, "black", (50, y + z), (550, y + z))
    pygame.draw.aaline(background, "black", (50, 120), (50, HEIGHT - 80))
    pygame.draw.aaline(background, "black", (550, 120), (550, HEIGHT - 80))
    pygame.draw.aaline(background, "black", (50, 120), (550, 120))
    pygame.draw.aaline(background, "black", (50, HEIGHT - 80), (550, HEIGHT - 80))
    screen.blit(background, (0, 0))
    pygame.display.flip()

# init_board(x, y)
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             cords = pygame.mouse.get_pos()
#             aproxed_cords = approx_cords(game_cords_match, cords)
#             screen.blit(x_mark, aproxed_cords)
#             tab_tuple = game_cords_match_reverse[aproxed_cords]
#
#     pygame.display.update()
#     clock.tick(60)  # limits FPS to 60
# pygame.quit()
