import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
dt = 0
background = pygame.image.load("grass.jpeg")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(background,(0,0))
    pygame.draw.aaline(background,"black",(200,150),(200,550))
    pygame.draw.aaline(background, "black", (50, 275), (550, 275))
    pygame.draw.aaline(background, "black", (50, 425), (550, 425))
    pygame.draw.aaline(background, "black", (400, 150), (400, 550))
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()