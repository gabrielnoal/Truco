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
    posição_x_baralho=(tela_largura/2) 
    posição_y_baralho=(tela_altura/2) -50

    altura_carta = tela_altura/6 
    largura_carta = tela_altura/9
    
    posição_x_carta1=(tela_largura/2)
    posição_y_carta1=(tela_altura/2)-50
    
    posição_x_carta2=(tela_largura/2)
    posição_y_carta2=(tela_altura/2)-50

    posição_x_carta3=(tela_largura/2)
    posição_y_carta3=(tela_altura/2)-50

    posição_x_carta4=(tela_largura/2)
    posição_y_carta4=(tela_altura/2)-50

    posição_x_carta5=(tela_largura/2)
    posição_y_carta5=(tela_altura/2)-50

    posição_x_carta6=(tela_largura/2)
    posição_y_carta6=(tela_altura/2)-50
    
    mover_carta_y=0
    mover_carta_x=0
    

    while not fim_do_app:
        while fim_do_jogo == True:
            pass
    
        for event in pygame.event.get():
            print (event)
            
            if event.type == pygame.QUIT:
                    fim_do_app = True
            if event.type == pygame.KEYDOWN:
                
                    
                if event.key == pygame.K_SPACE:
                        posição_y_carta1 = tela_altura- altura_carta
                        posição_y_carta2 = posição_y_carta1
                        posição_y_carta3 = posição_y_carta2

                        posição_y_carta4=0
                        posição_y_carta5=0
                        posição_y_carta6=0
                        
                        posição_x_carta1 -= largura_carta 
                        posição_x_carta2 = posição_x_carta1 + largura_carta + 20
                        posição_x_carta3 = posição_x_carta2 + largura_carta + 20
                        
                        posição_x_carta4 -= largura_carta 
                        posição_x_carta5 = posição_x_carta4 + largura_carta + 20
                        posição_x_carta6 = posição_x_carta5 + largura_carta + 20
                        
                        
                        
                
#        posição_y_carta+= mover_carta_y
#        posição_x_carta+= mover_carta_x
    
        costas_da_carta = pygame.transform.scale(costas_da_carta, (int(largura_carta),int(altura_carta)))
 
        tela_truco.fill(verde)
        tela_truco.fill(branco, rect=[posição_x_carta1,posição_y_carta1,largura_carta,altura_carta]) #Fill é mais usado por ser mais rapido
        tela_truco.fill(branco, rect=[posição_x_carta2,posição_y_carta2,largura_carta,altura_carta]) #Fill é mais usado por ser mais rapido
        tela_truco.fill(branco, rect=[posição_x_carta3,posição_y_carta3,largura_carta,altura_carta]) #Fill é mais usado por ser mais rapido
        
        tela_truco.fill(branco, rect=[posição_x_carta4,posição_y_carta4,largura_carta,altura_carta]) #Fill é mais usado por ser mais rapido
        tela_truco.fill(branco, rect=[posição_x_carta5,posição_y_carta5,largura_carta,altura_carta]) #Fill é mais usado por ser mais rapido
        tela_truco.fill(branco, rect=[posição_x_carta6,posição_y_carta6,largura_carta,altura_carta]) #Fill é mais usado por ser mais rapido

        tela_truco.blit(costas_da_carta, [posição_x_baralho,posição_y_baralho])

        pygame.display.update()
    

    pygame.display.update()
    pygame.quit()
    
loop_de_jogo()