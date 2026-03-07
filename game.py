import pygame
import os
from Game03.settings import *

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode(WIDTH, HEIGHT)


