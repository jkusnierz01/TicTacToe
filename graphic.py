import pygame
import sys
from TicTacToeLogic import *

WIDTH = 600
HEIGHT = 700
dt = 0
x = 145
y = 220

game_cords_match = {
    (0, 0): (96, 171),
    (0, 1): (193, 171),
    (0, 2): (292, 171),
    (0, 3): (395, 172),
    (0, 4): (497, 170),
    (1, 0): (95, 273),
    (1, 1): (193, 273),
    (1, 2): (294, 272),
    (1, 3): (391, 270),
    (1, 4): (496, 270),
    (2, 0): (96, 371),
    (2, 1): (194, 370),
    (2, 2): (291, 371),
    (2, 3): (393, 371),
    (2, 4): (497, 374),
    (3, 0): (95, 471),
    (3, 1): (195, 470),
    (3, 2): (294, 471),
    (3, 3): (393, 471),
    (3, 4): (497, 471),
    (4, 0): (95, 573),
    (4, 1): (195, 569),
    (4, 2): (294, 570),
    (4, 3): (395, 570),
    (4, 4): (495, 571)
}

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

init_board(x, y)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cords = pygame.mouse.get_pos()
            screen.blit(x_mark, cords)
    pygame.display.update()
    clock.tick(60)  # limits FPS to 60
pygame.quit()
