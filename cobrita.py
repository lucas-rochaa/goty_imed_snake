from cobrita_deff import macalocal, collision, text_objects, morte, pontuacao_tela
from loggin import 
import pygame
import random 
import time 

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

largura_tela = 600
altura_tela = 600
tela_jogo = pygame.display.set_mode((600,600))
pygame.display.set_caption('GOTY')



def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((largura_tela/2, altura_tela/2))
    tela_jogo.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    gameloop()

def pontuacao_tela(pontuacao):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Pontos: "+str(pontuacao),True, (255,255,255))
    tela_jogo.blit(text, (0,0))

def morte():
    message_display("Tu morreu")

clock = pygame.time.Clock()

def gameloop():

    cobrao = [(200, 200), (210, 200), (220,200)]
    cobrao_skin = pygame.Surface((10,10))
    cobrao_skin.fill((255,255,255))

    maca_pos = macalocal()
    maca = pygame.Surface((10,10))
    maca.fill((255,0,0))
    my_direction = LEFT
    pontuacao = 0

    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    my_direction = UP

                elif event.key ==  pygame.K_DOWN:
                    my_direction = DOWN

                elif event.key ==  pygame.K_LEFT:
                    my_direction = LEFT

                elif event.key ==  pygame.K_RIGHT:
                    my_direction = RIGHT

        if collision(cobrao[0], maca_pos):
            maca_pos = macalocal()
            cobrao.append((0,0))
            pontuacao = pontuacao + 1


        if cobrao[0][0] == 600 or cobrao[0][1] == 600 or cobrao[0][0] < 0 or cobrao[0][1] < 0:
            morte()

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

gameloop()