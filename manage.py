import pygame
# from PIL import Image
import io

from random import randint, choice

# pygame initialization
pygame.init()

# global variables (constants)
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
BG = pygame.image.load('bg.jpg')

# prepare plane image
PLANE_SIZE = (17, 17)
# plane_img = Image.open("plane.png")
# plane_img.thumbnail(PLANE_SIZE, Image.ANTIALIAS)
# plane_img.save("plane_1.png")

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
play = False
score = 0

plane_mask = []

start_ticks = pygame.time.get_ticks()


def change_level():
    change_bg()
    global plane_x, plane_y
    plane_y = randint(5, BG_HEIGHT + 5 - PLANE_SIZE[0])
    plane_x = randint(5, BG_WIDTH + 5 - PLANE_SIZE[1])

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

btn_font = pygame.font.SysFont('arial', 20)

# mainlooop
while not crashed:
    start_surf, start_rect = text_objects("Start!", btn_font, DARK)
    start_rect.center = ( (START_X + 15 +(50/2)), (START_Y+(BTN_H/2)) )

    reset_surf, reset_rect = text_objects("Reset!", btn_font, DARK)
    reset_rect.center = ( (RESET_X + 15 +(50/2)), (RESET_Y+(BTN_H/2)) )
    
    stop_surf, stop_rect = text_objects("Stop!", btn_font, RED)
    stop_rect.center = ( (STOP_X + 15 +(50/2)), (STOP_Y+(BTN_H/2)) )
    

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            # button start
            if start_rect.collidepoint(x, y):
                play = True
                score = 0
                start_ticks = pygame.time.get_ticks()

            if play:
                # button stop
                if stop_rect.collidepoint(x, y):
                    play = False
                    score = 0
                    start_ticks = pygame.time.get_ticks()
                    
                # button reset
                if reset_rect.collidepoint(x, y):
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


    pygame.draw.rect(screen, (226, 227, 223),(START_X,START_Y,BTN_W,BTN_H))
    screen.blit(start_surf, start_rect)
    if play:
        pygame.draw.rect(screen, (226, 227, 223),(RESET_X,RESET_Y,BTN_W,BTN_H))
        screen.blit(reset_surf, reset_rect)
        pygame.draw.rect(screen, (226, 227, 223),(STOP_X,STOP_Y,BTN_W,BTN_H))
        screen.blit(stop_surf, stop_rect)

    
    set_bg(5, 5)
    set_plane(plane_x, plane_y)

    pygame.display.update()
    clock.tick(30)


# exit game
if crashed:
    pygame.quit()

quit()
