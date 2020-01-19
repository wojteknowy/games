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

#paletka komputera
white = (0, 0, 0)
rocket_C_pos = (350, 40)
rocket_C = pygame.Surface([rocket_width, rocket_hight])
rocket_C.fill(white)
rocket_C_squ = rocket_C.get_rect()
rocket_C_squ.x = rocket_C_pos[0]
rocket_C_squ.y = rocket_C_pos[1]
speed_C = 5

#piłka
ball_width = 20
ball_height = 20
green = (0, 255, 0)
ball_speed_X = 6
ball_speed_Y = 6

ball = pygame.Surface([ball_width, ball_height], pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(ball, green, [0, 0, ball_height, ball_width])
ball_sql = ball.get_rect()
ball_sql.x = win_width / 2
ball_sql.y = win_height / 2

FPS = 30
fpsClock = pygame.time.Clock()

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #ruch piłki
    ball_sql.move_ip(ball_speed_X, ball_speed_Y)
    if ball_sql.right >= win_width:
        ball_speed_X *= -1
    if ball_sql.left <= 0:
        ball_speed_X *= -1

    if ball_sql.top <= 0:
       # ball_speed_Y *= -1
       ball_sql.x = win_width / 2
       ball_sql.y = win_height / 2

    if ball_sql.bottom >= win_height:
        ball_sql.x = win_width / 2
        ball_sql.y = win_height / 2

    # Dotknięcie paletki gracza

    if ball_sql.colliderect(rocket1_squ):
        ball_speed_Y *= -1
        ball_sql.bottom = rocket1_squ.top
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
     # Jak gra komputer
    if ball_sql.centerx > rocket_C_squ.centerx:
        rocket_C_squ.x += speed_C
    elif ball_sql.centerx < rocket_C_squ.centerx:
        rocket_C_squ.x -= speed_C

    if ball_sql.colliderect(rocket_C_squ):
        ball_speed_Y *= -1
        ball_sql.top = rocket_C_squ.bottom

    # Rysowanie

    win.fill((230, 255, 255))
    win.blit(rocket1, rocket1_squ)
    win.blit(rocket_C, rocket_C_squ)
    win.blit(ball, ball_sql)
    fpsClock.tick(FPS)
    pygame.display.update()

pygame.quit()