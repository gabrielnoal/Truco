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

tela_inicio = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('Truco')


altura_carta = tela_altura/4 
largura_carta = tela_altura/6


imagem_entrar = pygame.image.load('/home/moreira/Desktop/Truco-master/entrar.png')

gameLoop = True
while gameLoop:
	for  event in pygame.event.get():

		if (event.type==pygame.QUIT):
		
			gameLoop = False
	tela_inicio.fill(verde)
	tela_inicio.blit(imagem_entrar, [200,300])
	pygame.display.update()


pygame.quit()