import pygame
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

tela_inicio = pygame.display.set_mode((tela_largura,tela_altura))
pygame.display.set_caption('TrucOFF')





#def entrar no jogo():
	




def botao():
	tela_inicio.blit(imagem_entrar, [285,500])
	mouse_pos = pygame.mouse.get_pos()
	mouse_click = pygame.mouse.get_pressed()

	if (475 > mouse_pos[0] > 300):
		if (560 > mouse_pos[1] > 500):
			if mouse_click[0] == 1:
				tela_inicio.fill(verde)
				tela_inicio.blit(imagem_1, [0,25])
				tela_inicio.blit(imagem_2, [600,25])
				tela_inicio.blit(imagem_diamonds, [200,350])
				tela_inicio.blit(imagem_spades, [310,350])
				tela_inicio.blit(imagem_hearts, [420,350])
				tela_inicio.blit(imagem_clubs, [530,350])
				tela_inicio.blit(imagem_logo, [150,200])
				tela_inicio.blit(imagem_entrar_clicado, [285,500])
				print('você entrou no jogo')






gameLoop = True
while gameLoop:

	
	for  event in pygame.event.get():




		tela_inicio.fill(verde)
		tela_inicio.blit(imagem_1, [0,25])
		tela_inicio.blit(imagem_2, [600,25])
		tela_inicio.blit(imagem_diamonds, [200,350])
		tela_inicio.blit(imagem_spades, [310,350])
		tela_inicio.blit(imagem_hearts, [420,350])
		tela_inicio.blit(imagem_clubs, [530,350])
		tela_inicio.blit(imagem_logo, [150,200])
		
		botao()








		
		if (event.type==pygame.QUIT):
					
			gameLoop = False




	pygame.display.update()


pygame.quit()
