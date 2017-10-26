import pygame
from PIL import Image
import io

from random import randint, choice

# pygame initialization
pygame.init()


# global variables (constants)
BG_WIDTH = 640
BG_HEIGHT = 480

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = BG_HEIGHT + 10
# DISPLAY_HEIGHT = 600


WHITE = (236, 240, 241)
BLACK = (44, 62, 80)
RED = (231, 240, 241)

# load initial background
BG = pygame.image.load('bg.jpg')

# prepare plane image
PLANE_SIZE = (17, 17)
plane_img = Image.open("plane.png")
plane_img.thumbnail(PLANE_SIZE, Image.ANTIALIAS)
plane_img.save("plane_1.png")

PLANE = pygame.image.load('plane_1.png')


def change_bg():
    bx = choice([True, False])
    by = choice([True, False])

    if bx == by:
        bx, by = True, True
    global BG
    BG = pygame.transform.flip(BG, bx, by)


def set_bg(x, y):
    screen.blit(BG, (x, y))


def set_plane(x, y):
    screen.blit(PLANE, (x, y))


plane_x = (DISPLAY_WIDTH / 2)
plane_y = (DISPLAY_HEIGHT / 2)


screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

pygame.display.set_caption("Plane Fighter Simulator")

clock = pygame.time.Clock()

crashed = False
hit = False
score = 0

plane_mask = []

start_ticks = pygame.time.get_ticks()

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            x, y = event.pos
            p_x, p_y = PLANE_SIZE
            plane_rect = pygame.Rect(plane_x, plane_y, p_x, p_y)
            if plane_rect.collidepoint(x, y):
                change_bg()
                plane_y = randint(5, BG_HEIGHT + 5)
                plane_x = randint(5, BG_WIDTH + 5)
                print(plane_x, plane_y)
                score += 1

    screen.fill(WHITE)

    my_font = pygame.font.SysFont("monospace", 16)

    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    timertext = my_font.render("Timer = %.1f" % seconds, 1, (0, 0, 0))
    screen.blit(timertext, (BG_WIDTH + 35, 40))

    scoretext = my_font.render("Score = " + str(score), 1, (0, 0, 0))
    screen.blit(scoretext, (BG_WIDTH + 35, 10))

    set_bg(5, 5)
    set_plane(plane_x, plane_y)

    pygame.display.update()
    clock.tick(30)


if crashed:
    pygame.quit()

quit()
