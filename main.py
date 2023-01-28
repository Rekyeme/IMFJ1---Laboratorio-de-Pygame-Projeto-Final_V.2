import math
import sys

import numpy
import pygame
import numpy as np
from pygame.locals import *

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" ")

fpsClock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

V_POS = [0, 100]
V_DIR = [1, 0]
ANG = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    EVENTS = pygame.event.get()
    for event in EVENTS:
        if event.type == pygame.KEYDOWN:
            print(event.key)
            print(chr(event.key))
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                V_DIR = [0, 1]

    SCREEN.fill(WHITE)
    V_POS = np.add(V_POS, V_DIR)

    SPD = 3
    V_NORMALIZED = V_DIR/np.linalg.norm(V_DIR)
    V_VEL = np.multiply(SPD, V_NORMALIZED)
    V_POS = np.add(V_POS, V_VEL)

    V_GRAV_FORCE = [0, 9.8]
    V_POS = np.add(V_POS, V_GRAV_FORCE)

    ANG = ANG + numpy.pi / 21
    RAD = 150
    X = 250 + math.sin(ANG) * RAD
    Y = 250 + math.cos(ANG) * RAD

    pygame.draw.circle(SCREEN, BLACK, [X, Y], 21)

    pygame.display.update()
    fpsClock.tick(FPS)
