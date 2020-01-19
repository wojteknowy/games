import pygame
import sys
from pygame.locals import *

pygame.init()
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Pong")
# paletka gracza
rocket_width = 100
rocket_hight = 20
blue = (0, 0, 255)
rocket_1_pos = (350, 560)

# utworzenie paletki
rocket1 = pygame.Surface([rocket_width, rocket_hight])
rocket1.fill(blue)
rocket1_squ = rocket1.get_rect()
rocket1_squ.x = rocket_1_pos[0]
rocket1_squ.y = rocket_1_pos[1]
run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    # Sterowanie myszką
    if event.type == MOUSEMOTION:
        mouseX, mouseY = event.pos
    #Przesunięcie paletki gracza
        shift = mouseX - (rocket_width / 2)
    #Jeśli wykraczamy poza okno gry w prawo
        if shift > win_width - rocket_width:
            shift = win_width - rocket_width
    # Jeśli wykraczamy poza okno gry w lewo
        if shift < 0:
            shift = 0

        rocket1_squ.x = shift

    # Rysowanie

    win.fill((230, 255, 255))
    win.blit(rocket1, rocket1_squ)
    pygame.display.update()

pygame.quit()