import os
import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
pic = pygame.image.load("1.png")
screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
pygame.display.flip()
pygame.mixer.music.load("bgm.ogg")
pygame.mixer.music.play()
while True:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        pygame.display.quit()
        sys.exit()
    elif event.type == VIDEORESIZE:
        screen = pygame.display.set_mode(
            event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
        pygame.display.flip()
