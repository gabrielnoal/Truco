# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:52:08 2016

@author: Usuario
"""

import pygame
import time
from TrucON import Logica
jogo=Logica()

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

jogo.manilha()


#costas_da_carta = pygame.image.load("back_card.png")
#costas_da_carta = pygame.transform.scale(costas_da_carta, (largura_carta,altura_carta))


def loop_de_jogo():
    fim_do_app = False
    fim_do_jogo= False
    costas_da_carta = pygame.image.load("back_card.png")

    As_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_clubs.png")
    As_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_diamonds.png")
    As_copas     = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_hearts.png")
    As_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/01_of_spades.png")

    Dois_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_clubs.png")
    Dois_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_diamonds.png")
    Dois_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_hearts.png")
    Dois_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/02_of_spades.png")
    
    Tres_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_clubs.png")
    Tres_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_diamonds.png")
    Tres_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_hearts.png")
    Tres_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/03_of_spades.png")
    
    Quatro_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_clubs.png")
    Quatro_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_diamonds.png")
    Quatro_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_hearts.png")
    Quatro_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/04_of_spades.png")
    
    Cinco_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_clubs.png")
    Cinco_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_diamonds.png")
    Cinco_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_hearts.png")
    Cinco_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/05_of_spades.png")
    
    Seis_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_clubs.png")
    Seis_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_diamonds.png")
    Seis_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_hearts.png")
    Seis_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/06_of_spades.png")    

    Sete_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_clubs.png")
    Sete_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_diamonds.png")
    Sete_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_hearts.png")
    Sete_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/07_of_spades.png")    

    Valete_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_clubs_en.png")
    Valete_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_diamonds_en.png")
    Valete_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_hearts_en.png")
    Valete_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Jack_of_spades_en.png")
    
    Dama_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_clubs_en.png")
    Dama_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_diamonds_en.png")
    Dama_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_hearts_en.png")
    Dama_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/Queen_of_spades_en.png")
    
    Rei_paus = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_clubs_en.png")
    Rei_ouros = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_diamonds_en.png")
    Rei_copas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_diamonds_en.png")
    Rei_espadas = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Imagens Baralho/King_of_spades_en.png")
    
    imagens_baralho=[Quatro_ouros,Quatro_espadas,Quatro_copas,Quatro_paus,
                   Cinco_ouros,Cinco_espadas,Cinco_copas,Cinco_paus,
                   Seis_ouros,Seis_espadas,Seis_copas,Seis_paus,
                   Sete_ouros,Sete_espadas,Sete_copas,Sete_paus,
                   Dama_ouros,Dama_espadas,Dama_copas,Dama_paus,
                   Valete_ouros,Valete_espadas,Valete_copas,Valete_paus,
                   Rei_ouros,Rei_espadas,Rei_copas,Rei_paus,
                   As_ouros,As_espadas,As_copas,As_paus,
                   Dois_ouros,Dois_espadas,Dois_copas,Dois_paus,
                   Tres_ouros,Tres_espadas,Tres_copas,Tres_paus]
                   
                   
                   
    

    
    posição_x_baralho=(tela_largura/2) 
    posição_y_baralho=(tela_altura/2) -50

    altura_carta = tela_altura/6 
    largura_carta = tela_altura/9
    
    posição_x_carta1_1=(tela_largura/2)
    posição_y_carta1_1=(tela_altura/2)-50
    
    posição_x_carta1_2=(tela_largura/2)
    posição_y_carta1_2=(tela_altura/2)-50

    posição_x_carta1_3=(tela_largura/2)
    posição_y_carta1_3=(tela_altura/2)-50
    
#    posição_x_carta2_1=(tela_largura/2)
#    posição_y_carta2_1=(tela_altura/2)-50
#    
#    posição_x_carta2_2=(tela_largura/2)
#    posição_y_carta2_2=(tela_altura/2)-50
#    
#    posição_x_carta2_3=(tela_largura/2)
#    posição_y_carta2_3=(tela_altura/2)-50

    posição_x_carta3_1=(tela_largura/2)
    posição_y_carta3_1=(tela_altura/2)-50

    posição_x_carta3_2=(tela_largura/2)
    posição_y_carta3_2=(tela_altura/2)-50

    posição_x_carta3_3=(tela_largura/2)
    posição_y_carta3_3=(tela_altura/2)-50
    
    
#    posição_x_carta4_1=(tela_largura/2)
#    posição_y_carta4_1=(tela_altura/2)-50
#    
#    posição_x_carta4_2=(tela_largura/2)
#    posição_y_carta4_2=(tela_altura/2)-50
#    
#    posição_x_carta4_3=(tela_largura/2)
#    posição_y_carta4_3=(tela_altura/2)-50
    
#    mover_carta_y=0
#    mover_carta_x=0

    while not fim_do_app:
        
        while fim_do_jogo == True:
            pass
    
        for event in pygame.event.get():
#            print (event)
            
            if event.type == pygame.QUIT:
                    fim_do_app = True
            if event.type == pygame.KEYDOWN:
                
                    
                if event.key == pygame.K_SPACE:
                        posição_y_carta1_1 = tela_altura- altura_carta
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
                        
                
#        posição_y_carta+= mover_carta_y
#        posição_x_carta+= mover_carta_x
    
        costas_da_carta = pygame.transform.scale(costas_da_carta, (int(largura_carta),int(altura_carta)))
       
  
        
        manilha = imagens_baralho[jogo.vira]        
        manilha = pygame.transform.scale(manilha,(int(largura_carta),int(altura_carta)))
        
        tela_truco.fill(verde)
        
            
        tela_truco.blit(manilha, [posição_x_carta1_1,posição_y_carta1_1])        
        del imagens_baralho[jogo.vira]
        
        
#        tela_truco.blit(, [posição_x_carta1_1,posição_y_carta1_1])
#        tela_truco.blit(jogo.mão_jogador_0[1], [posição_x_carta1_2,posição_y_carta1_2])
#        tela_truco.blit(jogo.mão_jogador_0[2], [posição_x_carta1_3,posição_y_carta1_3])
        
#        tela_truco.blit(jogo.mão_jogador_1[0], [posição_x_carta3_1,posição_y_carta3_1])
#        tela_truco.blit(jogo.mão_jogador_1[1], [posição_x_carta3_2,posição_y_carta3_2])
#        tela_truco.blit(jogo.mão_jogador_1[2], [posição_x_carta3_3,posição_y_carta3_3])
#        
        tela_truco.blit(costas_da_carta, [posição_x_baralho,posição_y_baralho])

#        tela_truco.blit(costas_da_carta, [posição_x_carta3_3,posição_y_carta3_3])
#        tela_truco.blit(costas_da_carta, [posição_x_carta3_3,posição_y_carta3_3])
#        tela_truco.blit(costas_da_carta, [posição_x_carta3_3,posição_y_carta3_3])        
#        
#        tela_truco.blit(costas_da_carta, [posição_x_carta3_3,posição_y_carta3_3])
#        tela_truco.blit(costas_da_carta, [posição_x_carta3_3,posição_y_carta3_3])
#        tela_truco.blit(costas_da_carta, [posição_x_carta3_3,posição_y_carta3_3])

        tela_truco.blit(costas_da_carta, [posição_x_baralho,posição_y_baralho])
        
        pygame.display.update()
    

    pygame.display.update()
    pygame.quit()
    
loop_de_jogo()