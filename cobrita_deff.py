import pygame
import time
import random

from pygame.locals import *


def macalocal():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def text_objects(text,font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((largura_tela/2, altura_tela/2))
    tela_jogo.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()

def morte():
    message_display("Tu morreu")

def pontuacao_tela(pontuacao, tela):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pontos: "+str(pontuacao),True, (255,255,255))
    tela_jogo.blit(text, (0,0))

def text_objects(text,font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()