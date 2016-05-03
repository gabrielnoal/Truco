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

FPS=30

tela_largura=800
tela_altura=600
altura_carta = tela_altura/4
largura_carta = tela_altura/7
posição_y_carta=(tela_altura/2)-100
posição_x_carta=tela_largura/2
mover_carta_y=0
mover_carta_x=0

tela_truco = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Truco')

fim_do_jogo = False

while not fim_do_jogo:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.QUIT:
            fim_do_jogo = True
            
            
        if event.type == pygame.K_SPACE:
                mover_carta_y+=100
            
    posição_y_carta+= mover_carta_y
    posição_x_carta+= mover_carta_x

        
    tela_truco.fill(verde)
    tela_truco.fill(branco, rect=[posição_x_carta,posição_y_carta,largura_carta,altura_carta]) #Fill é mais usado por ser mais rapido
    
    pygame.display.update()
    

pygame.display.update()
pygame.quit()
quit()