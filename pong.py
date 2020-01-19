import pygame
import sys
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
# paletka gracza
rocket_width = 100
rocket_hight = 20
blue = (0, 0, 255)
rocket_1_pos = (350, 560)

# utworzenie paletki

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # Sterowanie

    # Rysowanie
    win.fill((230, 255, 255))

    pygame.display.update()

pygame.quit()