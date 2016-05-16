# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:12:27 2016

@author: Usuario
"""

import pygame
import time
from TrucON import Logica

class EstadoInterface:
    def __init__(self):
        self.reset()
    def reset(self):
        self.carta_1_1clicada = False
estado = EstadoInterface()

jogo=Logica(estado)

pygame.init()
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,150,0)

FPS=15

tela_largura=800
tela_altura=600



tela_truco = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Truco')

altura_carta = tela_altura/4 
largura_carta = tela_altura/6

costas_da_carta = pygame.image.load("back_card.png")
costas_da_carta = pygame.transform.scale(costas_da_carta, (int(largura_carta),int(altura_carta)))

As_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_clubs.png")
As_paus =pygame.transform.scale(As_paus, (int(largura_carta),int(altura_carta)))
As_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_diamonds.png")
As_ouros =pygame.transform.scale(As_ouros, (int(largura_carta),int(altura_carta)))
As_copas     = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_hearts.png")
As_copas = pygame.transform.scale(As_copas, (int(largura_carta),int(altura_carta)))
As_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_spades.png")
As_espadas = pygame.transform.scale(As_espadas, (int(largura_carta),int(altura_carta)))

Dois_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_clubs.png")
Dois_paus = pygame.transform.scale(Dois_paus, (int(largura_carta),int(altura_carta)))
Dois_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_diamonds.png")
Dois_ouros = pygame.transform.scale(Dois_ouros, (int(largura_carta),int(altura_carta)))
Dois_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_hearts.png")
Dois_copas = pygame.transform.scale(Dois_copas, (int(largura_carta),int(altura_carta)))
Dois_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_spades.png")
Dois_espadas = pygame.transform.scale(Dois_espadas, (int(largura_carta),int(altura_carta)))


Tres_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_clubs.png")
Tres_paus = pygame.transform.scale(Tres_paus, (int(largura_carta),int(altura_carta)))
Tres_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_diamonds.png")
Tres_ouros = pygame.transform.scale(Tres_ouros, (int(largura_carta),int(altura_carta)))
Tres_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_hearts.png")
Tres_copas = pygame.transform.scale(Tres_copas, (int(largura_carta),int(altura_carta)))
Tres_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_spades.png")
Tres_espadas = pygame.transform.scale(Tres_espadas, (int(largura_carta),int(altura_carta)))


Quatro_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_clubs.png")
Quatro_paus = pygame.transform.scale(Quatro_paus, (int(largura_carta),int(altura_carta)))
Quatro_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_diamonds.png")
Quatro_ouros = pygame.transform.scale(Quatro_ouros, (int(largura_carta),int(altura_carta)))
Quatro_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_hearts.png")
Quatro_copas = pygame.transform.scale(Quatro_copas, (int(largura_carta),int(altura_carta)))
Quatro_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_spades.png")
Quatro_espadas = pygame.transform.scale(Quatro_espadas, (int(largura_carta),int(altura_carta)))

Cinco_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_clubs.png")
Cinco_paus = pygame.transform.scale(Cinco_paus, (int(largura_carta),int(altura_carta)))
Cinco_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_diamonds.png")
Cinco_ouros = pygame.transform.scale(Cinco_ouros, (int(largura_carta),int(altura_carta)))
Cinco_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_hearts.png")
Cinco_copas = pygame.transform.scale(Cinco_copas, (int(largura_carta),int(altura_carta)))
Cinco_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_spades.png")
Cinco_espadas = pygame.transform.scale(Cinco_espadas, (int(largura_carta),int(altura_carta)))

Seis_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_clubs.png")
Seis_paus = pygame.transform.scale(Seis_paus, (int(largura_carta),int(altura_carta)))
Seis_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_diamonds.png")
Seis_ouros = pygame.transform.scale(Seis_ouros, (int(largura_carta),int(altura_carta)))
Seis_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_hearts.png")
Seis_copas = pygame.transform.scale(Seis_copas, (int(largura_carta),int(altura_carta)))
Seis_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_spades.png")    
Seis_espadas = pygame.transform.scale(Seis_espadas, (int(largura_carta),int(altura_carta)))

Sete_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_clubs.png")
Sete_paus = pygame.transform.scale(Sete_paus, (int(largura_carta),int(altura_carta)))
Sete_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_diamonds.png")
Sete_ouros = pygame.transform.scale(Sete_ouros, (int(largura_carta),int(altura_carta)))
Sete_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_hearts.png")
Sete_copas = pygame.transform.scale(Sete_copas, (int(largura_carta),int(altura_carta)))
Sete_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_spades.png")    
Sete_espadas = pygame.transform.scale(Sete_espadas, (int(largura_carta),int(altura_carta)))

Valete_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_clubs_en.png")
Valete_paus = pygame.transform.scale(Valete_paus, (int(largura_carta),int(altura_carta)))
Valete_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_diamonds_en.png")
Valete_ouros = pygame.transform.scale(Valete_ouros, (int(largura_carta),int(altura_carta)))
Valete_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_hearts_en.png")
Valete_copas = pygame.transform.scale(Valete_copas, (int(largura_carta),int(altura_carta)))
Valete_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_spades_en.png")
Valete_espadas = pygame.transform.scale(Valete_espadas, (int(largura_carta),int(altura_carta)))

Dama_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_clubs_en.png")
Dama_paus = pygame.transform.scale(Dama_paus, (int(largura_carta),int(altura_carta)))
Dama_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_diamonds_en.png")
Dama_ouros = pygame.transform.scale(Dama_ouros, (int(largura_carta),int(altura_carta)))
Dama_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_hearts_en.png")
Dama_copas = pygame.transform.scale(Dama_copas, (int(largura_carta),int(altura_carta)))
Dama_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_spades_en.png")
Dama_espadas = pygame.transform.scale(Dama_espadas, (int(largura_carta),int(altura_carta)))

Rei_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_clubs_en.png")
Rei_paus = pygame.transform.scale(Rei_paus, (int(largura_carta),int(altura_carta)))
Rei_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_diamonds_en.png")
Rei_ouros = pygame.transform.scale(Rei_ouros, (int(largura_carta),int(altura_carta)))
Rei_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_diamonds_en.png")
Rei_copas = pygame.transform.scale(Rei_copas, (int(largura_carta),int(altura_carta)))
Rei_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_spades_en.png")
Rei_espadas = pygame.transform.scale(Rei_espadas, (int(largura_carta),int(altura_carta)))

imagens_baralho=[Quatro_ouros, Quatro_espadas, Quatro_copas, Quatro_paus,
                   Cinco_ouros, Cinco_espadas, Cinco_copas, Cinco_paus,
                   Seis_ouros, Seis_espadas, Seis_copas, Seis_paus,
                   Sete_ouros, Sete_espadas, Sete_copas, Sete_paus,
                   Dama_ouros, Dama_espadas, Dama_copas, Dama_paus,
                   Valete_ouros, Valete_espadas, Valete_copas, Valete_paus,
                   Rei_ouros, Rei_espadas, Rei_copas, Rei_paus,
                   As_ouros, As_espadas, As_copas, As_paus,
                   Dois_ouros, Dois_espadas, Dois_copas, Dois_paus,
                   Tres_ouros, Tres_espadas, Tres_copas, Tres_paus]

#copiar lista/fazer um original = a=[]
# b = a[]

jogo.manilha()
print(jogo.vira)
jogo.distribuir_cartas()

imagem_manilha = imagens_baralho[jogo.vira]

carta_1_1 = imagens_baralho[jogo.carta_1_1]
del imagens_baralho[jogo.carta_1_1]
#print(carta_1_1_1)
carta_1_2 = imagens_baralho[jogo.carta_1_2]
del imagens_baralho[jogo.carta_1_2]
#print(carta_1_2)
carta_1_3 = imagens_baralho[jogo.carta_1_3]
del imagens_baralho[jogo.carta_1_3]
#print(carta_1_3)

carta_3_1 = imagens_baralho[jogo.carta_3_1]
del imagens_baralho[jogo.carta_3_1]
#print(carta_3_1)
carta_3_2 = imagens_baralho[jogo.carta_3_2]
del imagens_baralho[jogo.carta_3_2]
#print(carta_3_2)
carta_3_3 = imagens_baralho[jogo.carta_3_3]
del imagens_baralho[jogo.carta_3_3]
#print(carta_3_3)

posição_x_baralho=(tela_largura/2) 
posição_y_baralho=(tela_altura/2) -50

altura_carta = tela_altura/6 
largura_carta = tela_altura/9



def começando_partida():
    jogo.manilha()
    jogo.distribuir_cartas()
    
def loop_de_jogo():
    fim_do_app = False
    fim_do_jogo= False
    apertou_ESPAÇO = False
    '''Posição manilha'''
    posição_x_manilha = (tela_largura/2)
    posição_y_manilha = (tela_altura/2)-50
    '''Posiçoes das cartas do Jogador de baixo'''
    posição_x_carta1_1 = (tela_largura/2)
    posição_y_carta1_1 = (tela_altura/2)-50
    
    posição_x_carta1_2 = (tela_largura/2)
    posição_y_carta1_2 = (tela_altura/2)-50
    
    posição_x_carta1_3 = (tela_largura/2)
    posição_y_carta1_3 = (tela_altura/2)-50
    
    '''Posiçoes das cartas do Jogador de cima'''
    posição_x_carta3_1 = (tela_largura/2)
    posição_y_carta3_1 = (tela_altura/2)-50
    
    posição_x_carta3_2 = (tela_largura/2)
    posição_y_carta3_2 = (tela_altura/2)-50
    
    posição_x_carta3_3 = (tela_largura/2)
    posição_y_carta3_3 = (tela_altura/2)-50
    while not fim_do_app:
        while fim_do_jogo == True:
            pass


       
        for event in pygame.event.get():
#            print (event)
            
            if event.type == pygame.QUIT:
                    fim_do_app = True
            if event.type == pygame.KEYDOWN:
                
                    
                if event.key == pygame.K_SPACE:
                        if apertou_ESPAÇO == False:                   
                            posição_y_carta1_1 = tela_altura - altura_carta -50
                            posição_y_carta1_2 = posição_y_carta1_1 
                            posição_y_carta1_3 = posição_y_carta1_2 
    
                            posição_y_carta3_1=0
                            posição_y_carta3_2=0
                            posição_y_carta3_3=0
                            
                            posição_x_carta1_1 -= largura_carta 
                            posição_x_carta1_2 = posição_x_carta1_1 + largura_carta + 20
                            posição_x_carta1_3 = posição_x_carta1_2 + largura_carta + 20
                            
                            posição_x_carta3_1 -= largura_carta 
                            posição_x_carta3_2 = posição_x_carta3_1 + largura_carta + 20
                            posição_x_carta3_3 = posição_x_carta3_2 + largura_carta + 20
                            
                            
                            apertou_ESPAÇO = True
                if event.key == pygame.K_1:
                    posição_y_carta1_1=(tela_altura/2)-50
                    posição_x_carta1_1= posição_x_carta1_1=(tela_largura/2)+largura_carta+10
                if event.key == pygame.K_2:
                    posição_y_carta1_2=(tela_altura/2)-50
                    posição_x_carta1_2= posição_x_carta1_2=(tela_largura/2)+largura_carta+40
                if event.key == pygame.K_3:
                    posição_y_carta1_3=(tela_altura/2)-50
                    posição_x_carta1_3= posição_x_carta1_3=(tela_largura/2)+largura_carta+70
                    
                if event.key == pygame.K_4:
                    posição_y_carta3_1=(tela_altura/2)-50
                    posição_x_carta3_1= posição_x_carta3_1=(tela_largura/2)-largura_carta-70
                if event.key == pygame.K_5:
                    posição_y_carta3_2=(tela_altura/2)-50
                    posição_x_carta3_2= posição_x_carta3_2=(tela_largura/2)-largura_carta-40
                if event.key == pygame.K_6:
                    posição_y_carta3_3=(tela_altura/2)-50
                    posição_x_carta3_3= posição_x_carta3_3=(tela_largura/2)-largura_carta-10
                    
            tela_truco.fill(verde)
            tela_truco.blit(imagem_manilha, [posição_x_baralho,posição_y_baralho])

            tela_truco.blit(carta_1_1, [posição_x_carta1_1,posição_y_carta1_1])
            tela_truco.blit(carta_1_2, [posição_x_carta1_2,posição_y_carta1_2])
            tela_truco.blit(carta_1_3, [posição_x_carta1_3,posição_y_carta1_3])

            tela_truco.blit(carta_3_1, [posição_x_carta3_1,posição_y_carta3_1])
            tela_truco.blit(carta_3_2, [posição_x_carta3_2,posição_y_carta3_2])
            tela_truco.blit(carta_3_3, [posição_x_carta3_3,posição_y_carta3_3])
            if apertou_ESPAÇO == False:        
                tela_truco.blit(costas_da_carta,[posição_x_baralho,posição_y_baralho])
                    
            pygame.display.update()
    

    pygame.display.update()
    pygame.quit()
    
loop_de_jogo()
    
