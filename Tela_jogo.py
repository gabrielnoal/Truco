# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:52:08 2016

@author: Usuario
"""

import pygame
import time

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


#costas_da_carta = pygame.image.load("back_card.png")
#costas_da_carta = pygame.transform.scale(costas_da_carta, (largura_carta,altura_carta))


def loop_de_jogo():
    fim_do_app = False
    fim_do_jogo= False
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    costas_da_carta = pygame.image.load("back_card.png")
    
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
 
        tela_truco.fill(verde)

        
        tela_truco.blit(costas_da_carta, [posição_x_carta1_1,posição_y_carta1_1])
        tela_truco.blit(costas_da_carta, [posição_x_carta1_2,posição_y_carta1_2])
        tela_truco.blit(costas_da_carta, [posição_x_carta1_3,posição_y_carta1_3])
        
        tela_truco.blit(costas_da_carta, [posição_x_carta3_1,posição_y_carta3_1])
        tela_truco.blit(costas_da_carta, [posição_x_carta3_2,posição_y_carta3_2])
        tela_truco.blit(costas_da_carta, [posição_x_carta3_3,posição_y_carta3_3])
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