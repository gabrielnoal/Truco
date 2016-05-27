# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:12:27 2016

@author: Usuario
"""

import pygame
import time
from TrucOFF import Logica



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

altura_carta = tela_altura/4 
largura_carta = tela_altura/6

imagem_entrar = pygame.image.load('entrar.png')
imagem_entrar_clicado = pygame.image.load('entrar_clicado.png')
imagem_logo = pygame.image.load('logo.png')

imagem_1 = pygame.image.load('back_card.png')
imagem_1 = pygame.transform.rotate(imagem_1,25)

imagem_2 = pygame.image.load('back_card.png')
imagem_2 = pygame.transform.rotate(imagem_2,335)

imagem_diamonds = pygame.image.load('Diamonds.png')
imagem_spades = pygame.image.load('Spades.png')
imagem_hearts = pygame.image.load('Hearts.png')
imagem_clubs = pygame.image.load('Clubs.png')


botao_truco_0 = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Truco.png")
botao_truco_0_clicado = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Truco_clicado.png")

botao_truco_1 = pygame.transform.rotate(botao_truco_0, 180)
botao_truco_1_clicado = pygame.transform.rotate(botao_truco_0_clicado, 180)

botao_seis_0 = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Seis.png")
botao_seis_0_clicado = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Seis_clicado.png")

botao_seis_1 = pygame.transform.rotate(botao_seis_0, 180)
botao_seis_1_clicado = pygame.transform.rotate(botao_seis_0_clicado, 180)

botao_nove_0 = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Nove.png")
botao_nove_0_clicado = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Nove_clicado.png")

botao_nove_1 = pygame.transform.rotate(botao_nove_0, 180)
botao_nove_1_clicado = pygame.transform.rotate(botao_nove_0_clicado, 180)

botao_doze_0 = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Doze.png")
botao_doze_0_clicado = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Doze_clicado.png")

botao_doze_1 = pygame.transform.rotate(botao_doze_0, 180)
botao_doze_1_clicado = pygame.transform.rotate(botao_doze_0_clicado, 180)

botao_cair_0 = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Cair.png")
botao_cair_0_clicado = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Cair_clicado.png")

botao_cair_1 = pygame.transform.rotate(botao_cair_0, 180)
botao_cair_1_clicado = pygame.transform.rotate(botao_cair_0_clicado, 180)

botao_correr_0 = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Correr.png")
botao_correr_0_clicado = pygame.image.load("C:/Users/Usuario/Documents/GitHub/Truco/Correr_clicado.png")

botao_correr_1 = pygame.transform.rotate(botao_correr_0, 180)
botao_correr_1_clicado = pygame.transform.rotate(botao_correr_0_clicado, 180)

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

imagens_baralho_original=[Quatro_ouros, Quatro_espadas, Quatro_copas, Quatro_paus,
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
# b = a[:]



posição_x_baralho=(tela_largura/2) 
posição_y_baralho=(tela_altura/2) -50

posição_mesa_esquerda = [(tela_largura/2)-largura_carta-40, (tela_altura/2)-50]
posição_mesa_direita = [(tela_largura/2)+largura_carta+40 , (tela_altura/2)-50]

altura_carta = tela_altura/6 
largura_carta = tela_altura/9

posição_botao_truco_0 = [10, tela_altura - 95]
posição_botao_truco_1 = [145 , 45]

posição_botao_correr_0 = [(posição_botao_truco_0[0] + 145), posição_botao_truco_0[1]]
posição_botao_correr_1 = [(posição_botao_truco_1[0] - 145), posição_botao_truco_1[1]]

largura_botao = 135
altura_botao = 65

lixo = -500


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

score_0 = "Score: {0}".format(jogo.ponto_jogo_jogador_0)
score_1 = "Score: {0}".format(jogo.ponto_jogo_jogador_1)

jogador_0_pediu_truco = False
jogador_1_pediu_truco = False


def botao_inicio():
	tela_truco.blit(imagem_entrar, [285,500])
	mouse_pos = pygame.mouse.get_pos()
	mouse_click = pygame.mouse.get_pressed()

	if (475 > mouse_pos[0] > 300):
		if (560 > mouse_pos[1] > 500):
			if mouse_click[0] == 1:
				tela_truco.fill(verde)
				tela_truco.blit(imagem_1, [0,25])
				tela_truco.blit(imagem_2, [600,25])
				tela_truco.blit(imagem_diamonds, [200,350])
				tela_truco.blit(imagem_spades, [310,350])
				tela_truco.blit(imagem_hearts, [420,350])
				tela_truco.blit(imagem_clubs, [530,350])
				tela_truco.blit(imagem_logo, [150,200])
				tela_truco.blit(imagem_entrar_clicado, [285,500])
				return True
    
def funcao_truco_0():
    tela_truco.blit(botao_truco_0, [posição_botao_truco_0[0], posição_botao_truco_0[1]])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    if (posição_botao_truco_0[0] < mouse_pos[0] < posição_botao_truco_0[0] + largura_botao):
        if (posição_botao_truco_0[1] < mouse_pos[1] < posição_botao_truco_0[1] + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_truco_0_clicado, [posição_botao_truco_0[0], posição_botao_truco_0[1]])
                pygame.display.update()
                jogo.troca_jogador()
                return True
            
def funcao_truco_1():
    tela_truco.blit(botao_truco_1, [posição_botao_truco_1[0], posição_botao_truco_1[1]])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    if (posição_botao_truco_1[0] < mouse_pos[0] < posição_botao_truco_1[0] + largura_botao):
        if (posição_botao_truco_1[1] < mouse_pos[1] < posição_botao_truco_1[1] + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_truco_1_clicado, [posição_botao_truco_1[0], posição_botao_truco_1[1]])
                pygame.display.update()
                jogo.troca_jogador()
                return True
            
def funcao_cair_0():
    tela_truco.blit(botao_cair_0, [posição_botao_truco_0[0], posição_botao_truco_0[1]])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_truco_0[0] < mouse_pos[0] < posição_botao_truco_0[0] + largura_botao):
        if (posição_botao_truco_0[1] < mouse_pos[1] < posição_botao_truco_0[1] + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_cair_0_clicado, [posição_botao_truco_0[0], posição_botao_truco_0[1]])
                return True
                
def funcao_cair_1():
    tela_truco.blit(botao_cair_1, [posição_botao_truco_1[0], posição_botao_truco_1[1]])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_truco_1[0] < mouse_pos[0] < posição_botao_truco_1[0] + largura_botao):
        if (posição_botao_truco_1[1] < mouse_pos[1] < posição_botao_truco_1[1] + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_cair_1_clicado, [posição_botao_truco_1[0], posição_botao_truco_1[1]])
                return True              
                                
def funcao_correr_0():
    tela_truco.blit(botao_correr_0, [posição_botao_correr_0[0],posição_botao_correr_0[1]])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_0[0] < mouse_pos[0] < posição_botao_correr_0[0] + largura_botao):
        if (posição_botao_correr_0[1] < mouse_pos[1] < posição_botao_correr_0[1] + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_correr_0_clicado, [posição_botao_correr_0[0], posição_botao_correr_0[1]])
                return True

def funcao_correr_1():
    tela_truco.blit(botao_correr_1, [posição_botao_correr_1[0],posição_botao_correr_1[1]])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_1[0] < mouse_pos[0] < posição_botao_correr_1[0] + largura_botao):
        if (posição_botao_correr_1[1] < mouse_pos[1] < posição_botao_correr_1[1] + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_correr_1_clicado, [posição_botao_correr_1[0], posição_botao_correr_1[1]])
                return True
                
def funcao_seis_1():
    tela_truco.blit(botao_seis_1, [posição_botao_correr_1[0],posição_botao_correr_1[1] + 75])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_1[0] < mouse_pos[0] < posição_botao_correr_1[0] + largura_botao):
        if (posição_botao_correr_1[1] + 75 < mouse_pos[1] < posição_botao_correr_1[1] + 75 + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_seis_1_clicado, [posição_botao_correr_1[0],posição_botao_correr_1[1] + 75])
                jogo.troca_jogador()
                return True
                
def funcao_seis_0():
    tela_truco.blit(botao_seis_0, [posição_botao_correr_0[0],posição_botao_correr_0[1] - 75])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_0[0] < mouse_pos[0] < posição_botao_correr_0[0] + largura_botao):
        if (posição_botao_correr_0[1] - 75 < mouse_pos[1] < posição_botao_correr_0[1] - 75 + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_seis_0_clicado, [posição_botao_correr_1[0],posição_botao_correr_1[1] - 75])
                jogo.troca_jogador()
                return True
                
def funcao_nove_1():
    tela_truco.blit(botao_nove_1, [posição_botao_correr_1[0],posição_botao_correr_1[1] + 75])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_1[0] < mouse_pos[0] < posição_botao_correr_1[0] + largura_botao):
        if (posição_botao_correr_1[1] + 75 < mouse_pos[1] < posição_botao_correr_1[1] + 75 + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_nove_1_clicado, [posição_botao_correr_1[0],posição_botao_correr_1[1] + 75])
                jogo.troca_jogador()
                return True
                
def funcao_nove_0():
    tela_truco.blit(botao_nove_0, [posição_botao_correr_0[0],posição_botao_correr_0[1] - 75])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_0[0] < mouse_pos[0] < posição_botao_correr_0[0] + largura_botao):
        if (posição_botao_correr_0[1] - 75 < mouse_pos[1] < posição_botao_correr_0[1] - 75 + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_nove_0_clicado, [posição_botao_correr_1[0],posição_botao_correr_1[1] - 75])
                jogo.troca_jogador()
                return True
                
def funcao_doze_1():
    tela_truco.blit(botao_doze_1, [posição_botao_correr_1[0],posição_botao_correr_1[1] + 75])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_1[0] < mouse_pos[0] < posição_botao_correr_1[0] + largura_botao):
        if (posição_botao_correr_1[1] + 75 < mouse_pos[1] < posição_botao_correr_1[1] + 75 + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_doze_1_clicado, [posição_botao_correr_1[0],posição_botao_correr_1[1] + 75])
                jogo.troca_jogador()
                return True
                
def funcao_doze_0():
    tela_truco.blit(botao_doze_0, [posição_botao_correr_0[0],posição_botao_correr_0[1] - 75])
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if (posição_botao_correr_0[0] < mouse_pos[0] < posição_botao_correr_0[0] + largura_botao):
        if (posição_botao_correr_0[1] - 75 < mouse_pos[1] < posição_botao_correr_0[1] - 75 + altura_botao):
            if mouse_click[0] == 1:
                tela_truco.blit(botao_doze_0_clicado, [posição_botao_correr_1[0],posição_botao_correr_1[1] - 75])
                jogo.troca_jogador()
                return True

        
                

def text_objects(text,color,size):
    if size =="small":
        textSurface = smallfont.render(text, True, color)
    elif size =="medium":
        textSurface = medfont.render(text, True, color)
    if size =="large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def messege_to_screen_0(msg,color, x, y, y_displace=0, size= "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center= x, y + y_displace
    tela_truco.blit(textSurf, textRect)
    
    
def messege_to_screen_1(msg,color, x, y, y_displace=0, size= "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center= x, y + y_displace
    textSurf = pygame.transform.rotate(textSurf, 180)
    tela_truco.blit(textSurf, textRect)
    
def loop_de_jogo():
    fim_do_app = False
    fim_do_jogo= False
    apertou_ESPAÇO = False
    inicio_da_partida = True
    jogador_que_começa = 0    
    inicio = True
    
        

    '''Posição manilha'''
    posição_x_manilha = posição_x_baralho
    posição_y_manilha = posição_y_baralho
    '''Posiçoes das cartas do Jogador de baixo'''
    posição_x_carta1_1 = posição_x_baralho
    posição_y_carta1_1 = posição_y_baralho
    
    posição_x_carta1_2 = posição_x_baralho
    posição_y_carta1_2 = posição_y_baralho
    
    posição_x_carta1_3 = posição_x_baralho
    posição_y_carta1_3 = posição_y_baralho
    
    '''Posiçoes das cartas do Jogador de cima'''
    posição_x_carta3_1 = posição_x_baralho
    posição_y_carta3_1 = posição_y_baralho
    
    posição_x_carta3_2 = posição_x_baralho
    posição_y_carta3_2 = posição_y_baralho
    
    posição_x_carta3_3 = posição_x_baralho
    posição_y_carta3_3 = posição_y_baralho
    while not fim_do_app:
        while inicio == True:        
            
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    pygame.quit()
                        
                        
            tela_truco.fill(verde)
            tela_truco.blit(imagem_1, [0,25])
            tela_truco.blit(imagem_2, [600,25])
            tela_truco.blit(imagem_diamonds, [200,350])
            tela_truco.blit(imagem_spades, [310,350])
            tela_truco.blit(imagem_hearts, [420,350])
            tela_truco.blit(imagem_clubs, [530,350])
            tela_truco.blit(imagem_logo, [150,200])
            botao_inicio()
            pygame.display.update()
            if botao_inicio() == True:
                inicio = False
            
        if jogo.ponto_jogo_jogador_0 >= 12 or jogo.ponto_jogo_jogador_1 >= 12:
            fim_do_jogo = True
            while fim_do_jogo == True:
                pass

        if inicio_da_partida == True:
            jogo.reset()
            jogo.jogador = jogador_que_começa
            jogou_carta_1_1 = False
            jogou_carta_1_2 = False
            jogou_carta_1_3 = False
            
            jogou_carta_3_1 = False
            jogou_carta_3_2 = False
            jogou_carta_3_3 = False
            
            jogador_0_pediu_truco = False
            jogador_1_pediu_truco = False
            
            jogador_0_pediu_seis = False            
            jogador_1_pediu_seis = False
            
            jogador_0_pediu_nove = False            
            jogador_1_pediu_nove = False            

            jogador_0_pediu_doze = False            
            jogador_1_pediu_doze = False
            
            cartas_0_bloqueadas = True
            cartas_1_bloqueadas = True
            
            
            
            apertou_ESPAÇO = False
            imagens_baralho = imagens_baralho_original[:]
            
            jogo.manilha()
            print(jogo.vira)
            jogo.distribuir_cartas()
            
            
            imagem_manilha = imagens_baralho[jogo.vira]

            carta_1_1 = imagens_baralho[jogo.carta_1_1]
            carta_1_2 = imagens_baralho[jogo.carta_1_2]
            carta_1_3 = imagens_baralho[jogo.carta_1_3]    
            carta_3_1 = imagens_baralho[jogo.carta_3_1]
            carta_3_2 = imagens_baralho[jogo.carta_3_2]
            carta_3_3 = imagens_baralho[jogo.carta_3_3]
            
            '''Posição manilha'''
            posição_x_manilha = posição_x_baralho
            posição_y_manilha = posição_y_baralho
            '''Posiçoes das cartas do Jogador de baixo'''
            posição_x_carta1_1 = posição_x_baralho
            posição_y_carta1_1 = posição_y_baralho
            
            posição_x_carta1_2 = posição_x_baralho
            posição_y_carta1_2 = posição_y_baralho
    
            posição_x_carta1_3 = posição_x_baralho
            posição_y_carta1_3 = posição_y_baralho
    
            '''Posiçoes das cartas do Jogador de cima'''
            posição_x_carta3_1 = posição_x_baralho
            posição_y_carta3_1 = posição_y_baralho
    
            posição_x_carta3_2 = posição_x_baralho
            posição_y_carta3_2 = posição_y_baralho
    
            posição_x_carta3_3 = posição_x_baralho
            posição_y_carta3_3 = posição_y_baralho
            
            inicio_da_partida = False
       
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
                            
                            cartas_0_bloqueadas = False
                            cartas_1_bloqueadas = False
                            
                            apertou_ESPAÇO = True
                    
                if cartas_0_bloqueadas == False:
                    if jogo.jogador == 0:            
                        if event.key == pygame.K_1:
                            if jogou_carta_1_1 ==False:
                                posição_y_carta1_1= posição_mesa_direita[1]
                                posição_x_carta1_1= posição_mesa_direita[0]
                                jogo.mesa.append(jogo.mao_jogador_0[0])
                                jogo.mao_jogador_0[0]=-1
                                jogo.troca_jogador()
                                print(jogo.mesa)
                                jogou_carta_1_1 = True
                                pygame.display.update()
                                
                                    
                        if event.key == pygame.K_2:
                            if jogou_carta_1_2 == False:                    
                                posição_y_carta1_2= posição_mesa_direita[1]
                                posição_x_carta1_2= posição_mesa_direita[0]
                                jogo.mesa.append(jogo.mao_jogador_0[1])
                                jogo.mao_jogador_0[1]=-1
                                jogo.troca_jogador()
                                print(jogo.mesa)
                                jogou_carta_1_2 = True
                                pygame.display.update()
    
        
                        if event.key == pygame.K_3:
                            if jogou_carta_1_3 == False:                    
                                posição_y_carta1_3= posição_mesa_direita[1]
                                posição_x_carta1_3= posição_mesa_direita[0]
                                jogo.mesa.append(jogo.mao_jogador_0[2])
                                jogo.mao_jogador_0[2]=-1
                                jogo.troca_jogador()
                                print(jogo.mesa)
                                jogou_carta_1_3 = True
                                pygame.display.update()
                                
                if cartas_1_bloqueadas == False:                
                    if jogo.jogador == 1:
                        if event.key == pygame.K_4:
                            if jogou_carta_3_1 == False:
                                posição_y_carta3_1= posição_mesa_esquerda[1]
                                posição_x_carta3_1= posição_mesa_esquerda[0]
                                jogo.mesa.append(jogo.mao_jogador_1[0])
                                jogo.mao_jogador_1[0]=-1
                                jogo.troca_jogador()
                                print(jogo.mesa)
                                jogou_carta_3_1 = True
        
                        if event.key == pygame.K_5:
                            if jogou_carta_3_2 == False:
                                posição_y_carta3_2= posição_mesa_esquerda[1]
                                posição_x_carta3_2= posição_mesa_esquerda[0]
                                jogo.mesa.append(jogo.mao_jogador_1[1])
                                jogo.mao_jogador_1[1]=-1
                                jogo.troca_jogador()
                                print(jogo.mesa)
                                jogou_carta_3_2 = True
    
    
                        if event.key == pygame.K_6:
                            if jogou_carta_3_3 == False:
                                posição_y_carta3_3= posição_mesa_esquerda[1]
                                posição_x_carta3_3= posição_mesa_esquerda[0]
                                jogo.mesa.append(jogo.mao_jogador_1[2])
                                jogo.mao_jogador_1[2]=-1
                                jogo.troca_jogador()
                                print(jogo .mesa)
                                jogou_carta_3_3 = True
                                
                            

                                
                                
            if len(jogo.mesa)==2:
                if jogo.mao_jogador_0[0] == -1:
                    posição_x_carta1_1 = lixo                    
                if jogo.mao_jogador_0[1] == -1:
                    posição_x_carta1_2 = lixo
                if jogo.mao_jogador_0[2] == -1:
                    posição_x_carta1_3 = lixo
                    
                if jogo.mao_jogador_1[0] == -1:
                    posição_x_carta3_1 = lixo
                if jogo.mao_jogador_1[1] == -1:
                    posição_x_carta3_2 = lixo
                if jogo.mao_jogador_1[2] == -1:
                    posição_x_carta3_3 = lixo
                    
                jogo.verifica_ganhador()
                jogo.limpa_jogadas()
            
                
            tela_truco.fill(verde)
            tela_truco.blit(imagem_manilha, [posição_x_manilha,posição_y_manilha])
            if apertou_ESPAÇO == True:
                if jogo.jogador == 0:
                    if jogo.mao_jogador_0[0] != -1:
                        tela_truco.blit(carta_1_1, [posição_x_carta1_1,posição_y_carta1_1])
                    if jogo.mao_jogador_0[1] != -1:                    
                        tela_truco.blit(carta_1_2, [posição_x_carta1_2,posição_y_carta1_2])
                    if jogo.mao_jogador_0[2] != -1:
                        tela_truco.blit(carta_1_3, [posição_x_carta1_3,posição_y_carta1_3])
                    
                    if jogo.mao_jogador_1[0] != -1:                
                        tela_truco.blit(costas_da_carta,[posição_x_carta3_1,posição_y_carta3_1])
                    if jogo.mao_jogador_1[0] == -1:
                        tela_truco.blit(carta_3_1, [posição_x_carta3_1,posição_y_carta3_1])
                    
                    if jogo.mao_jogador_1[1] != -1:            
                        tela_truco.blit(costas_da_carta,[posição_x_carta3_2,posição_y_carta3_2])
                    if jogo.mao_jogador_1[1] == -1:
                        tela_truco.blit(carta_3_2, [posição_x_carta3_2,posição_y_carta3_2])
    
                    if jogo.mao_jogador_1[2] != -1:
                        tela_truco.blit(costas_da_carta,[posição_x_carta3_3,posição_y_carta3_3])
                    if jogo.mao_jogador_1[2] == -1:
                        tela_truco.blit(carta_3_3, [posição_x_carta3_3,posição_y_carta3_3])
                        
                    
                    if jogo.valor_partida == 1:
                        if funcao_truco_0() == True:
                            jogador_0_pediu_truco = True
                            
                        elif funcao_correr_0() == True:
                            jogo.correr_truco()

                            
                        if jogador_1_pediu_truco == True:
                            cartas_0_bloqueadas = True
                            if funcao_cair_0() == True:
                                jogo.cair_truco()
                                cartas_0_bloqueadas = False
                            elif funcao_correr_0() == True:
                                jogo.correr_truco()
                                cartas_0_bloqueadas = False
                            elif funcao_seis_0() == True:
                                jogo.valor_partida = 3
                                jogador_0_pediu_seis = True

                    elif jogo.valor_partida == 3 and jogo.jogador == 0:
                        if funcao_correr_0() == True:
                            jogo.correr_truco()
                            
                        if jogador_1_pediu_truco == True:
                            if funcao_seis_0() == True:
                                jogador_0_pediu_seis = True
                                
                        if jogador_1_pediu_seis == True:
                            cartas_0_bloqueadas = True
                            if funcao_cair_0() == True:
                                jogo.cair_seis()
                                cartas_0_bloqueadas = False
                            elif funcao_correr_0() == True:
                                jogo.correr_truco()
                                cartas_0_bloqueadas = False
                            elif funcao_nove_0() == True:
                                jogo.valor_partida = 6
                                jogador_0_pediu_nove = True
                                
                    elif jogo.valor_partida == 6 and jogo.jogador == 0:
                        if funcao_correr_0() == True:
                            jogo.correr_truco()
                            
                        if jogador_1_pediu_nove == True:
                            cartas_0_bloqueadas = True
                            if funcao_cair_0() == True:
                                jogo.cair_nove()
                                cartas_0_bloqueadas = False
                            elif funcao_correr_0() == True:
                                jogo.correr_truco()
                                cartas_0_bloqueadas = False
                            elif funcao_doze_0() == True:
                                jogo.valor_partida = 9
                                jogador_0_pediu_doze = True
                                
                    elif jogo.valor_partida == 9 and jogo.jogador == 0:
                        if funcao_correr_0() == True:
                            jogo.correr_truco()
                        
                        if jogador_1_pediu_doze == True:
                            cartas_0_bloqueadas = True
                            if funcao_cair_0() == True:
                                jogo.cair_doze()
                                cartas_0_bloqueadas = False
                            elif funcao_correr_0() == True:
                                jogo.correr_truco()
                                cartas_0_bloqueadas = False
                        
                                               
                    pygame.display.update()

                            
                        
                            
                       
                elif jogo.jogador == 1:
                    # Verifica se o jogador 1 ja jogou a carta, se não jogou blit a carta para ele ver
                    if jogo.mao_jogador_1[2] != -1:                    
                        tela_truco.blit(carta_3_3, [posição_x_carta3_3,posição_y_carta3_3])                    
                    if jogo.mao_jogador_1[1] != -1:
                        tela_truco.blit(carta_3_2, [posição_x_carta3_2,posição_y_carta3_2])

                    if jogo.mao_jogador_1[0] != -1:
                        tela_truco.blit(carta_3_1, [posição_x_carta3_1,posição_y_carta3_1])
                    
                        
    
                    if jogo.mao_jogador_0[0] != -1:
                        tela_truco.blit(costas_da_carta,[posição_x_carta1_1,posição_y_carta1_1])
                    if jogo.mao_jogador_0[0] == -1:
                        tela_truco.blit(carta_1_1, [posição_x_carta1_1,posição_y_carta1_1])
    
                    if jogo.mao_jogador_0[1] != -1:
                        tela_truco.blit(costas_da_carta,[posição_x_carta1_2,posição_y_carta1_2])
                    if jogo.mao_jogador_0[1] == -1:
                        tela_truco.blit(carta_1_2, [posição_x_carta1_2,posição_y_carta1_2])
                           
                    if jogo.mao_jogador_0[2] != -1:
                        tela_truco.blit(costas_da_carta,[posição_x_carta1_3,posição_y_carta1_3])
                    if jogo.mao_jogador_0[2] == -1:
                        tela_truco.blit(carta_1_3, [posição_x_carta1_3,posição_y_carta1_3])
                        
                    if jogo.valor_partida == 1:
                        if funcao_truco_1() == True:
                            jogador_1_pediu_truco = True
                            
                        elif funcao_correr_1() == True:
                            jogo.correr_truco()

                            
                        if jogador_0_pediu_truco == True:
                            cartas_1_bloqueadas = True
                            if funcao_cair_1() == True:
                                jogo.cair_truco()
                                cartas_1_bloqueadas = False
                            elif funcao_correr_1() == True:
                                jogo.correr_truco()
                                cartas_1_bloqueadas = False
                            elif funcao_seis_1() == True:
                                jogo.valor_partida = 3
                                jogador_1_pediu_seis = True

                    elif jogo.valor_partida == 3 and jogo.jogador == 1:
                        if funcao_correr_1() == True:
                            jogo.correr_truco()
                            
                        if jogador_0_pediu_truco == True:
                            if funcao_seis_1() == True:
                                jogador_1_pediu_seis = True
                                
                        if jogador_0_pediu_seis == True:
                            cartas_1_bloqueadas = True
                            if funcao_cair_1() == True:
                                jogo.cair_seis()
                                cartas_1_bloqueadas = False
                            elif funcao_correr_1() == True:
                                jogo.correr_truco()
                                cartas_1_bloqueadas = False
                            elif funcao_nove_1() == True:
                                jogo.valor_partida = 6
                                jogador_1_pediu_nove = True
                                
                    elif jogo.valor_partida == 6 and jogo.jogador == 1:
                        if funcao_correr_1() == True:
                            jogo.correr_truco()
                            
                        if jogador_0_pediu_nove == True:
                            cartas_1_bloqueadas = True
                            if funcao_cair_1() == True:
                                jogo.cair_nove()
                                cartas_1_bloqueadas = False
                            elif funcao_correr_1() == True:
                                jogo.correr_truco()
                                cartas_1_bloqueadas = False
                            elif funcao_doze_1() == True:
                                jogo.valor_partida = 9
                                jogador_1_pediu_doze = True
                                
                    elif jogo.valor_partida == 9 and jogo.jogador == 1:
                        if funcao_correr_1() == True:
                            jogo.correr_truco()
                        
                        if jogador_0_pediu_doze == True:
                            cartas_1_bloqueadas = True
                            if funcao_cair_1() == True:
                                jogo.cair_doze()
                                cartas_1_bloqueadas = False
                            elif funcao_correr_1() == True:
                                jogo.correr_truco()
                                cartas_1_bloqueadas = False
                            
                    pygame.display.update()


            
            if apertou_ESPAÇO == False:        
                tela_truco.blit(costas_da_carta,[posição_x_baralho,posição_y_baralho])
                
            if jogo.ponto_rodada_jogador_0 >= 2:
                if jogo.ponto_rodada_jogador_0 >= jogo.ponto_rodada_jogador_1:
                    print('Jogador 0 ganhou a rodada!')
                    print()
                    jogo.ponto_jogo_jogador_0 += jogo.valor_partida
                    print('Pontos na partida jogador 0:', jogo.ponto_jogo_jogador_0)
                    print('Pontos na partida jogador 1:', jogo.ponto_jogo_jogador_1)
                    jogo.rodada = 4
                    jogo.mao_jogador_0=[]
                    jogo.mao_jogador_1=[]
                    jogo.mesa=[]
                    jogo.ponto_rodada_jogador_0=0
                    jogo.ponto_rodada_jogador_1=0   
                    jogo.valor_partida=1
                    jogo.truco = False
                    inicio_da_partida = True
                    if jogador_que_começa == 0:
                        jogador_que_começa = 1
                    elif jogador_que_começa == 1:
                        jogador_que_começa = 0
                
            if jogo.ponto_rodada_jogador_1 >= 2 and jogo.ponto_rodada_jogador_0 != jogo.ponto_rodada_jogador_1 :
                if jogo.ponto_rodada_jogador_1 > jogo.ponto_rodada_jogador_0:                
                    print('Jogador 1 ganhou a rodada!')
                    print()
                    jogo.ponto_jogo_jogador_1 += jogo.valor_partida
                    print('Pontos na partida jogador 1:',jogo.ponto_jogo_jogador_1)
                    print('Pontos na partida jogador 0:',jogo.ponto_jogo_jogador_0)
                    jogo.rodada = 4
                    jogo.ponto_rodada_jogador_0=0
                    jogo.ponto_rodada_jogador_1=0   
                    jogo.valor_partida=1
                    jogo.truco = False
                    inicio_da_partida = True
                    if jogador_que_começa == 0:
                        jogador_que_começa = 1
                    elif jogador_que_começa == 1:
                        jogador_que_começa = 0

            messege_to_screen_0("Score: {0}".format(jogo.ponto_jogo_jogador_0) , preto, (tela_largura - 100), (tela_altura- 75), y_displace=0, size= "small")
            messege_to_screen_1("Score: {0}".format(jogo.ponto_jogo_jogador_1) , preto, (tela_largura - 100), (75), y_displace=0, size= "small")        


            pygame.display.update()
                        
            
            
    

    pygame.display.update()
    pygame.quit()
    
loop_de_jogo()
    
