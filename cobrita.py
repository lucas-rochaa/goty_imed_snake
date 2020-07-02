from cobrita_deff import salva_pontos, gameloop, macalocal, collision, text_objects, morte, pontuacao_tela
import pygame
import random 
import time 

try:
    arquivo = open("jogologing.txt","a")
    nome = input("Digite seu nome: ")
    arquivo.write("\n")
    arquivo.write("======================================== \n")
    arquivo.write("              NOVO JOGADOR               \n")
    arquivo.write("======================================== \n")
    arquivo.write("Jogador: ")
    arquivo.write(nome)
    arquivo.write("\n")
    arquivo.close()
    gameloop()

except:
    print("Algo deu errado :O")

        





