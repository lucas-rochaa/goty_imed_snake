from cobrita_deff import salva_pontos, gameloop, macalocal, collision, text_objects, morte, pontuacao_tela
import pygame
import random 
import time 

try:
    arquivo = open("jogologing.txt","a")
    nome = input("Digite seu nome: ")
    arquivo.write("Jogador: ")
    arquivo.write(nome)
    arquivo.write("\n")
    gameloop()
    arquivo.close()

        
except:
    print("Algo deu errado :O")



