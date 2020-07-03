import pygame
import time
import random

from pygame.locals import *

largura_tela = 600
altura_tela = 600
tela_jogo = pygame.display.set_mode((600,600))
pygame.display.set_caption('GOTY')

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

def morte():
    message_display("Tu morreu")

def pontuacao_tela(pontuacao):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pontos: "+str(pontuacao),True, (255,255,255))
    tela_jogo.blit(text, (0,0))

def text_objects(text,font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def salva_pontos(pontuacao):
    arquivo = open("jogologing.txt", "a")
    arquivo.write("pontuacao: ")
    arquivo.write(str(pontuacao))
    arquivo.write("\n")
    print(pontuacao)


def gameloop():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    pygame.init()

    largura_tela = 600
    altura_tela = 600
    tela_jogo = pygame.display.set_mode((600,600))
    pygame.display.set_caption('GOTY')

    clock = pygame.time.Clock()
    cobrao = [(200, 200), (210, 200), (220,200)]
    cobrao_skin = pygame.Surface((10,10))
    cobrao_skin.fill((255,255,255))

    maca_pos = macalocal()
    maca = pygame.Surface((10,10))
    maca.fill((255,0,0))
    my_direction = RIGHT
    pontuacao = 0
    tempo = 20
    

    while True:
        clock.tick(tempo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if my_direction == DOWN:
                        pass
                    else:
                        my_direction = UP

                elif event.key ==  pygame.K_DOWN:
                    if my_direction == UP:
                        pass
                    else:
                        my_direction = DOWN

                elif event.key ==  pygame.K_LEFT:
                    if my_direction == RIGHT:
                        pass
                    else:
                        my_direction = LEFT

                elif event.key ==  pygame.K_RIGHT:
                    if my_direction == LEFT:
                        pass
                    else:
                        my_direction = RIGHT

        if collision(cobrao[0], maca_pos):
            maca_pos = macalocal()
            cobrao.append((0,0))
            pontuacao = pontuacao + 1

            if pontuacao == 5:
                tempo = tempo = 25
            else:
                pass
            if pontuacao == 10:
                tempo = tempo = 30
            else: 
                pass
            if pontuacao == 20:
                tempo = tempo  = 35
            else:
                pass
            if pontuacao == 30:
                tempo = tempo = 40
            else:
                pass
            
        if cobrao[0][0] == 600 or cobrao[0][1] == 600 or cobrao[0][0] < 0 or cobrao[0][1] < 0:
            salva_pontos(pontuacao)
            morte()
            gameloop()     
        else:
            pass

        for l in range(1, len(cobrao) - 1):
            if cobrao[0][0] == cobrao[l][0] and cobrao[0][1] == cobrao[l][1]:
                salva_pontos(pontuacao)
                morte()
                gameloop()     



        for i in range(len(cobrao) - 1, 0, -1):
            cobrao[i] = (cobrao[i-1][0], cobrao[i-1][1])

        if my_direction == UP:
            cobrao[0] = (cobrao[0][0], cobrao[0][1] - 10)

        elif my_direction == DOWN:
            cobrao[0] = (cobrao[0][0], cobrao[0][1] + 10)

        elif my_direction == RIGHT:
            cobrao[0] = (cobrao[0][0] + 10, cobrao[0][1])

        elif my_direction == LEFT:
            cobrao[0] = (cobrao[0][0] - 10, cobrao[0][1])

        tela_jogo.fill((0,0,0))
        tela_jogo.blit(maca, maca_pos)
        
        pontuacao_tela(pontuacao)

        for pos in cobrao:
            tela_jogo.blit(cobrao_skin,pos)
            
        pygame.display.update()
