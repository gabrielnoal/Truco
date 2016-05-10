# -*- coding: utf-8 -*-
"""
Created on Fri May  6 14:24:44 2016

@author: Usuario
"""
import random
class Logica:
    def __init__(self):
        self.baralho = ['Quatro_ouros','Quatro_espadas','Quatro_copas','Quatro_paus',
                   'Cinco_ouros','Cinco_espadas','Cinco_copas','Cinco_paus',
                   'Seis_ouros','Seis_espadas','Seis_copas','Seis_paus',
                   'Sete_ouros','Sete_espadas','Sete_copas','Sete_paus',
                   'Dama_ouros','Dama_espadas','Dama_copas','Dama_paus',
                   'Valete_ouros','Valete_espadas','Valete_copas','Valete_paus',
                   'Rei_ouros','Rei_espadas','Rei_copas','Rei_paus',
                   'As_ouros','As_espadas','As_copas','As_paus',
                   'Dois_ouros','Dois_espadas','Dois_copas','Dois_paus',
                   'Tres_ouros','Tres_espadas','Tres_copas','Tres_paus']
                   
        self.dic_baralho = {'Quatro_ouros':1,'Quatro_espadas':1,'Quatro_copas':1,'Quatro_paus':1,
                            'Cinco_ouros':2,'Cinco_espadas':2,'Cinco_copas':2,'Cinco_paus':2,
                            'Seis_ouros':3,'Seis_espadas':3,'Seis_copas':3,'Seis_paus':3,
                            'Sete_ouros':4,'Sete_espadas':4,'Sete_copas':4,'Sete_paus':4,
                            'Dama_ouros':5,'Dama_espadas':5,'Dama_copas':5,'Dama_paus':5,
                            'Valete_ouros':6,'Valete_espadas':6,'Valete_copas':6,'Valete_paus':6,
                            'Rei_ouros':7,'Rei_espadas':7,'Rei_copas':7,'Rei_paus':7,
                            'As_ouros':8,'As_espadas':8,'As_copas':8,'As_paus':8,
                            'Dois_ouros':9,'Dois_espadas':9,'Dois_copas':9,'Dois_paus':9,
                            'Tres_ouros':10,'Tres_espadas':10,'Tres_copas':10,'Tres_paus':10}
        self.jogador=0
        self.rodada=1
        self.mão_jogador_0=[]
        self.mão_jogador_1=[]
        self.mesa=[]
        self.ponto_rodada_jogador_0=0
        self.ponto_rodada_jogador_1=0   
        self.ponto_jogo_jogador_0 = 0
        self.ponto_jogo_jogador_1 = 0
        self.truco=1
        
    def manilha(self):
        self.vira = random.randint(0,39)
        self.vira_carta=self.baralho[self.vira]
        self.a = self.vira_carta.split('_')
        self.b = self.a[1]
        #SE a vira for 3 fiz esse código para não dar erro
        if self.vira in [36,37,38,39]:
            self.pika = self.baralho[0]
            self.espadilha = self.baralho[1]
            self.copa = self.baralho[2]
            self.zap = self.baralho[3]
            
            print("A vira é o: {0}".format(self.baralho[self.vira]))
            del self.baralho[self.vira]
            self.dic_baralho[self.pika]=11
            self.dic_baralho[self.espadilha]=12
            self.dic_baralho[self.copa]=13
            self.dic_baralho[self.zap]=14
            return

        else:
            if self.b == 'ouros':
                self.pika = self.baralho[self.vira+4]
                self.espadilha = self.baralho[self.vira+5]
                self.copa = self.baralho[self.vira+6]
                self.zap = self.baralho[self.vira+7]
                    
            if self.b == 'espadas':
                self.pika = self.baralho[self.vira+3]
                self.espadilha = self.baralho[self.vira+4]
                self.copa = self.baralho[self.vira+5]
                self.zap = self.baralho[self.vira+6]
                                
            if self.b == 'copas':
                self.pika = self.baralho[self.vira+2]
                self.espadilha = self.baralho[self.vira+3]
                self.copa = self.baralho[self.vira+4]
                self.zap = self.baralho[self.vira+5]
            
            if self.b == 'paus':
                self.pika = self.baralho[self.vira+1]
                self.espadilha = self.baralho[self.vira+2]
                self.copa = self.baralho[self.vira+3]
                self.zap = self.baralho[self.vira+4]
                   
            print("A vira é o: {0}".format(self.baralho[self.vira]))
            del self.baralho[self.vira]
            self.dic_baralho[self.pika]=11
            self.dic_baralho[self.espadilha]=12
            self.dic_baralho[self.copa]=13
            self.dic_baralho[self.zap]=14

            return
            
    def distribuir_cartas(self):
        self.carta_1=random.randint(0,39-1)
        self.mão_jogador_0.append(self.baralho[self.carta_1])
        del self.baralho[self.carta_1]
            
        self.carta_2=random.randint(0,39-2)
        self.mão_jogador_0.append(self.baralho[self.carta_2])
        del self.baralho[self.carta_2]
            
        self.carta_3=random.randint(0,39-3)
        self.mão_jogador_0.append(self.baralho[self.carta_3])
        del self.baralho[self.carta_3]
            
        self.carta_4=random.randint(0,39-4)
        self.mão_jogador_1.append(self.baralho[self.carta_4])
        del self.baralho[self.carta_4]
            
        self.carta_5=random.randint(0,39-5)
        self.mão_jogador_1.append(self.baralho[self.carta_5])
        del self.baralho[self.carta_5]
            
        self.carta_6=random.randint(0,39-6)
        self.mão_jogador_1.append(self.baralho[self.carta_6])
        del self.baralho[self.carta_6]
        
#        print (self.baralho)

        return self.mão_jogador_0,self.mão_jogador_1
            
    def troca_jogador(self):
        if self.jogador == 0:
            self.jogador =1
            return 
        else:
            self.jogador =0
            return 
            
    def joga_carta(self):                
        while self.jogador ==0:
            self.pergunta= input('Jogador 1: Qual carta quer jogar? ')
            #self.pedir_truco()
            if self.pergunta=='1':
                if self.mão_jogador_0[0]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mão_jogador_0[0])
                    self.mão_jogador_0[0]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='2':
                if self.mão_jogador_0[1]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mão_jogador_0[1])
                    self.mão_jogador_0[1]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='3':
                if self.mão_jogador_0[2]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mão_jogador_0[2])
                    self.mão_jogador_0[2]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
        
        while self.jogador ==1:
            self.pergunta= input('Jogador 2: Qual carta quer jogar? ')
            self.pedir_truco()
            if self.pergunta=='1':
                if self.mão_jogador_1[0]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mão_jogador_1[0])
                    self.mão_jogador_1[0]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='2':
                if self.mão_jogador_1[1]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mão_jogador_1[1])
                    self.mão_jogador_1[1]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='3':
                if self.mão_jogador_1[2]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mão_jogador_1[2])
                    self.mão_jogador_1[2]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
        
    def limpa_jogadas(self):
        self.mesa=[]        
        print(self.mesa)
        
    def jogador_1_venceu9(self):
        pass
        
    def verifica_ganhador(self):
        carta_mesa_0 = self.dic_baralho[self.mesa[0]]
        carta_mesa_1 = self.dic_baralho[self.mesa[1]]
        
        if self.rodada==1:
            if carta_mesa_0 > carta_mesa_1:
                self.ponto_rodada_jogador_0+=1
                self.rodada += 1
                return
            elif carta_mesa_0 < carta_mesa_1:
                self.troca_jogador()
                self.ponto_rodada_jogador_1+=1
                self.rodada+=1
                return
            else:
                self.troca_jogador()
                self.ponto_rodada_jogador_0+=1
                self.ponto_rodada_jogador_1+=1                
                if carta_mesa_0 > carta_mesa_1:
                    self.ponto_rodada_jogador_1+=1
                    return
                elif carta_mesa_0 < carta_mesa_1:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_0+=1
                    return
                else:
                    if carta_mesa_0 > carta_mesa_1:
                        self.ponto_rodada_jogador_0+=1
                        return
                    elif carta_mesa_0 < carta_mesa_1:
                        self.troca_jogador()
                        self.ponto_rodada_jogador_1+=1
                        return
                    else:
                        if carta_mesa_0 > carta_mesa_1:
                            self.ponto_rodada_jogador_0+=1
                            return
                        elif carta_mesa_0 < carta_mesa_1:
                            self.troca_jogador()
                            self.ponto_rodada_jogador_1+=1
                            self.rodada+=1
                            return
                        else:
                            self.ponto_jogo_jogador_0+=1
                            self.ponto_jogo_jogador_1+=1
                            return
                        
        elif self.rodada==2:
            if carta_mesa_0 > carta_mesa_1:
                self.ponto_rodada_jogador_0+=1
                self.rodada+=1
                return
                    
            elif carta_mesa_0 < carta_mesa_1:
                self.troca_jogador()
                self.ponto_rodada_jogador_1+=1
                self.rodada+=1
                return
                    
            else:
                if self.jogador == 1:
                    self.ponto_jogo_jogador_0+=self.truco
                    print("Fim da rodada, empatou")
                    return
                else:
                    self.ponto_jogo_jogador_1+=self.truco
                    print("Fim da rodada, empatou")
                    return
        elif self.rodada==3:
            if carta_mesa_0 > carta_mesa_1:
                self.ponto_rodada_jogador_0+=1
                self.rodada+=1
                return
            
            elif carta_mesa_0 < carta_mesa_1:
                self.troca_jogador()
                self.ponto_rodada_jogador_1+=1
                self.rodada+=1
                return
            else:
                if self.jogador == 1:
                    self.ponto_jogo_jogador_0+=self.truco
                    print("Fim da rodada, empatou")
                    return
                else:
                    self.ponto_jogo_jogador_1+=self.truco
                    print("Fim da rodada, empatou")
                    return
                    
        if self.ponto_rodada_jogador_0== 2:
            self.ponto_jogo_jogador_0+=self.truco
            return

        elif self.ponto_rodada_jogador_1== 2:
            self.ponto_jogo_jogador_1 += self.truco
            return
        
        return
        
    def placar(self):
        print ("Jogador 1: {0} e Jogador 2: {1}".format(self.ponto_jogo_jogador_0,self.ponto_jogo_jogador_1))
        return
        
    def verifica_ganhador_partida(self):
        if self.ponto_jogo_jogador_0<=12:
            return ("Jogador 1 ganhou de {0} a {1}".format(self.ponto_jogo_jogador_0,self.ponto_jogo_jogador_1))
        elif self.ponto_jogo_jogador_1<=12:
            return ("Jogador 2 ganhou de {0} a {1}".format(self.ponto_jogo_jogador_1,self.ponto_jogo_jogador_0))
        else:
            return -1
    

        
    def pedir_truco(self):
        if self.pergunta=="truco" or self.pergunta=="Truco":
            print('O outro jogador pediu Truco.')
            self.pergunta= input ('Quer cair no Truco? sim/não/6')
            if self.pergunta == "sim" or self.pergunta == "Sim" or self.pergunta == 's' or self.pergunta == 'S':
                self.truco=3

            elif self.pergunta== "6":
                print('O outro jogador pediu 6.')
                self.pergunta= input ('Quer cair no 6? sim/não/9')
                if self.pergunta == "sim" or self.pergunta == "Sim" or self.pergunta == 's' or self.pergunta == 'S':
                    self.truco=6
                    if self.pergunta== "9":
                        print('O outro jogador pediu 9.')
                        self.pergunta= input ('Quer cair no 9? sim/não/9')
                        if self.pergunta == "sim" or self.pergunta == "Sim" or self.pergunta == 's' or self.pergunta == 'S':
                            self.truco="9"
                            if self.pergunta==12:
                                print('O outro jogador pediu 9.')
                                self.pergunta= input ('Quer cair no 9? sim/não/9')
                                if self.pergunta == "sim" or self.pergunta == "Sim" or self.pergunta == 's' or self.pergunta == 'S':
                                    self.truco==12
                                elif self.pergunta == "nao" or self.pergunta == 'não' or self.pergunta == "Nao" or self.pergunta == 'Não' or self.pergunta =='n' or self.pergunta =='N':
                                    self.troca_jogador()
                                    if self.jogador==0:
                                        self.ponto_jogo_jogador_0+=9
                                    else:
                                        self.ponto_jogo_jogador_1+=9
                        elif self.pergunta == "nao" or self.pergunta == 'não' or self.pergunta == "Nao" or self.pergunta == 'Não' or self.pergunta =='n' or self.pergunta =='N':
                            self.troca_jogador()
                            if self.jogador==0:
                                self.ponto_jogo_jogador_0+=6
                            else:
                                self.ponto_jogo_jogador_1+=6
                elif self.pergunta == "nao" or self.pergunta == 'não' or self.pergunta == "Nao" or self.pergunta == 'Não' or self.pergunta =='n' or self.pergunta =='N':
                    self.troca_jogador()
                    if self.jogador==0:
                        self.ponto_jogo_jogador_0+=3
                    else:
                        self.ponto_jogo_jogador_1+=3
            
            
            
#            elif self.pergunta == "nao" or self.pergunta == 'não' or self.pergunta == "Nao" or self.pergunta == 'Não' or self.pergunta =='n' or self.pergunta =='N':
            else:            
                self.troca_jogador()
                if self.jogador==0:
                    self.ponto_rodada_jogador_0=3
                    self.ponto_jogo_jogador_0+=1
                    return
                else:
                    self.ponto_rodada_jogador_1=3
                    self.ponto_jogo_jogador_1+=1
                    return
            
            return self.pergunta
                    

    def gameloop(self):        
        self.manilha()
        self.distribuir_cartas()
        print(self.mão_jogador_0,self.mão_jogador_1)
        self.joga_carta()
        self.joga_carta()
        self.verifica_ganhador()
        self.limpa_jogadas()
        self.verifica_ganhador_partida()
        
        
        print(self.mão_jogador_0,self.mão_jogador_1)
        self.joga_carta()
        self.joga_carta()
        self.verifica_ganhador()
        self.limpa_jogadas()
        self.verifica_ganhador_partida()

        print(self.mão_jogador_0,self.mão_jogador_1)
        self.joga_carta()
        self.joga_carta()
        self.verifica_ganhador()
        self.limpa_jogadas()
        self.verifica_ganhador_partida()
        
        return self.placar()


jogo=Logica()
jogo.gameloop()


#print(jogo.distribuir_cartas())
#
#
#print(jogo.joga_carta())
#print(jogo.joga_carta())
#print(jogo.verifica_ganhador())
#print(jogo.ponto_rodada_jogador_0)
#print(jogo.ponto_rodada_jogador_1)
#
#print(jogo.mão_jogador_0,jogo.mão_jogador_1)
#print(jogo.joga_carta())
#print(jogo.joga_carta())
#print(jogo.verifica_ganhador())
#print(jogo.ponto_rodada_jogador_0)
#print(jogo.ponto_rodada_jogador_1)
#
#
#print(jogo.mão_jogador_0,jogo.mão_jogador_1)
#print(jogo.joga_carta())
#print(jogo.joga_carta())
#print(jogo.verifica_ganhador())
#print(jogo.ponto_rodada_jogador_0)
#print(jogo.ponto_rodada_jogador_1)
#
#
#print(jogo.placar())
