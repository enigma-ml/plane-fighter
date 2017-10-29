import pygame
# from PIL import Image
from random import randint, choice

from sprites import TextBtn

# pygame initialization
pygame.init()

# global variables
BG_WIDTH = 640
BG_HEIGHT = 480

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = BG_HEIGHT + 10

# POS
LEFT = BG_WIDTH + 20

# BUTTONS

BTN_W = 80
BTN_H = 26

START_X = 684
START_Y = 400

RESET_X = 684
RESET_Y = 430

STOP_X = 684
STOP_Y = 460

# COLOR
WHITE = (236, 240, 241)
CREAM = (217, 203, 158)
GREY = (55, 65, 64)
DARK = (42, 44, 43)
BLACK = (30, 30, 32)
RED = (220, 53, 34)

# load initial background
MAP = pygame.image.load('bg.jpg')

# prepare plane image
PLANE_SIZE = (17, 17)
# plane_img = Image.open("plane.png")
# plane_img.thumbnail(PLANE_SIZE, Image.ANTIALIAS)
# plane_img.save("plane_1.png")

PLANE = pygame.image.load('plane_1.png')


def change_map():
    bx = choice([True, False])
    by = choice([True, False])

    if bx == by:
        bx, by = True, True
    global MAP
    MAP = pygame.transform.flip(MAP, bx, by)


def set_map(x, y):
    screen.blit(MAP, (x, y))


def set_plane(x, y):
    screen.blit(PLANE, (x, y))


def change_level():
    change_map()
    global plane_x, plane_y
    plane_y = randint(5, BG_HEIGHT + 5 - PLANE_SIZE[0])
    plane_x = randint(5, BG_WIDTH + 5 - PLANE_SIZE[1])


plane_x = (DISPLAY_WIDTH / 2)
plane_y = (DISPLAY_HEIGHT / 2)

screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

pygame.display.set_caption("Plane Fighter Simulator")

clock = pygame.time.Clock()

crashed = False
hit = False
play = False
score = 0

plane_mask = []

start_ticks = pygame.time.get_ticks()


# mainlooop
while not crashed:

    start_btn = TextBtn(text="Start!", pos=(START_X, START_Y), size=(BTN_W, BTN_H), font_size=20, font='arial',
                        bg=(226, 227, 223), text_color=DARK)

    reset_btn = TextBtn(text="Reset!", pos=(RESET_X, RESET_Y), size=(BTN_W, BTN_H), font_size=20, font='arial',
                        bg=(226, 227, 223), text_color=DARK)

    stop_btn = TextBtn(text="Stop!", pos=(STOP_X, STOP_Y), size=(BTN_W, BTN_H), font_size=20, font='arial',
                       bg=(226, 227, 223), text_color=RED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # button start
            if start_btn.rect.collidepoint(x, y):
                play = True
                score = 0
                start_ticks = pygame.time.get_ticks()

            if play:
                # button stop
                if stop_btn.rect.collidepoint(x, y):
                    play = False
                    score = 0
                    start_ticks = pygame.time.get_ticks()

                # button reset
                if reset_btn.rect.collidepoint(x, y):
                    change_level()
                    score = 0
                    start_ticks = pygame.time.get_ticks()

                # plane hit
                p_x, p_y = PLANE_SIZE
                plane_rect = pygame.Rect(plane_x, plane_y, p_x, p_y)
                if plane_rect.collidepoint(x, y):
                    change_level()
                    score += 1
                    start_ticks = pygame.time.get_ticks()

    screen.fill(WHITE)

    my_font = pygame.font.SysFont("monospace", 16)

    if play:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        timertext = my_font.render("Timer = %.1f" % seconds, 1, BLACK)
        screen.blit(timertext, (LEFT, 40))

    scoretext = my_font.render("Score = " + str(score), 1, RED)
    screen.blit(scoretext, (LEFT, 10))

    start_btn.draw(screen)

    if play:
        reset_btn.draw(screen)
        stop_btn.draw(screen)

    set_map(5, 5)
    set_plane(plane_x, plane_y)

    pygame.display.update()
    clock.tick(30)

# exit game
if crashed:
    pygame.quit()

quit()
