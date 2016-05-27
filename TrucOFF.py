    
    
    
    
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
        self.mao_jogador_0=[]
        self.mao_jogador_1=[]
        self.mesa=[]
        self.ponto_rodada_jogador_0=0
        self.ponto_rodada_jogador_1=0   
        self.ponto_jogo_jogador_0 = 0
        self.ponto_jogo_jogador_1 = 0
        self.valor_partida=1
        self.truco = False
        
    def manilha(self):
        self.vira = random.randint(0,39)
        self.vira_carta=self.baralho[self.vira]
        a = self.vira_carta.split('_')
        b = a[1]
        #SE a vira for 3 fiz esse código para não dar erro
        if self.vira in [36,37,38,39]:
            pika= self.baralho[0]
            espadilha = self.baralho[1]
            copas = self.baralho[2]
            zap = self.baralho[3]
            
            print("A vira é o: {0}".format(self.baralho[self.vira]))
            self.baralho[self.vira] = "-1"
            self.dic_baralho[pika]=11
            self.dic_baralho[espadilha]=12
            self.dic_baralho[copas ]=13
            self.dic_baralho[zap]=14
#            print(self.baralho)            
            return
            
            
        else:
            if b == 'ouros':
                pika = self.baralho[self.vira+4]
                espadilha = self.baralho[self.vira+5]
                copas = self.baralho[self.vira+6]
                zap = self.baralho[self.vira+7]
                    
            if b == 'espadas':
                pika = self.baralho[self.vira+3]
                espadilha = self.baralho[self.vira+4]
                copas = self.baralho[self.vira+5]
                zap = self.baralho[self.vira+6]
                                
            if b == 'copas':
                pika = self.baralho[self.vira+2]
                espadilha = self.baralho[self.vira+3]
                copas = self.baralho[self.vira+4]
                zap = self.baralho[self.vira+5]
            
            if b == 'paus':
                pika = self.baralho[self.vira+1]
                espadilha = self.baralho[self.vira+2]
                copas = self.baralho[self.vira+3]
                zap = self.baralho[self.vira+4]
                   
            print("A vira é o: {0}".format(self.baralho[self.vira]))
            self.baralho[self.vira] = "-1"
            self.dic_baralho[pika]=11
            self.dic_baralho[espadilha]=12
            self.dic_baralho[copas ]=13
            self.dic_baralho[zap]=14
#            print(self.baralho)            
            return
            
    def distribuir_cartas(self):
#        print(len(self.baralho))
        self.carta_1_1 = random.randint(0,39)
        while self.baralho[self.carta_1_1] == "-1":
            self.carta_1_1 = random.randint(0,39)
        self.mao_jogador_0.append(self.baralho[self.carta_1_1]) # Mudar as outras cartas
        self.baralho[self.carta_1_1] = "-1"
        
        self.carta_1_2 = random.randint(0,39)
        while self.baralho[self.carta_1_2] == "-1":
            self.carta_1_2 = random.randint(0,39)          
        self.mao_jogador_0.append(self.baralho[self.carta_1_2])
        self.baralho[self.carta_1_2] = "-1"
        
        self.carta_1_3 = random.randint(0,39)
        while self.baralho[self.carta_1_3] == "-1":
            self.carta_1_3 = random.randint(0,39)
        self.mao_jogador_0.append(self.baralho[self.carta_1_3])
        self.baralho[self.carta_1_3] = "-1"
        
        self.carta_3_1 = random.randint(0,39)
        while self.baralho[self.carta_3_1] == "-1":
            self.carta_3_1 = random.randint(0,39)
        self.mao_jogador_1.append(self.baralho[self.carta_3_1])
        self.baralho[self.carta_3_1] = "-1"
        
        self.carta_3_2 = random.randint(0,39)
        while self.baralho[self.carta_3_2] == "-1":
            self.carta_3_2 = random.randint(0,39)
        self.mao_jogador_1.append(self.baralho[self.carta_3_2])
        self.baralho[self.carta_3_2] = "-1"
        
        self.carta_3_3 = random.randint(0,39)
        while self.baralho[self.carta_3_3] == "-1":
            self.carta_3_3 = random.randint(0,39)          
        self.mao_jogador_1.append(self.baralho[self.carta_3_3])
        self.baralho[self.carta_3_3] = "-1"
        
        print (self.mao_jogador_0)
        print (self.mao_jogador_1)

        return self.mao_jogador_0,self.mao_jogador_1
            
    def troca_jogador(self):
        if self.jogador == 0:
            self.jogador =1
        else:
            self.jogador =0
        return
            
    def joga_carta(self):                
        while self.jogador ==0:
            self.pergunta= input('Jogador 1: Qual carta quer jogar? ')
            self.pedir_truco()
            if self.pergunta=='1':
                if self.mao_jogador_0[0]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mao_jogador_0[0])
                    self.mao_jogador_0[0]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='2':
                if self.mao_jogador_0[1]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mao_jogador_0[1])
                    self.mao_jogador_0[1]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='3':
                if self.mao_jogador_0[2]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mao_jogador_0[2])
                    self.mao_jogador_0[2]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
        
        while self.jogador ==1:
            self.pergunta= input('Jogador 2: Qual carta quer jogar? ')
            self.pedir_truco()
            if self.pergunta=='1':
                if self.mao_jogador_1[0]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mao_jogador_1[0])
                    self.mao_jogador_1[0]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='2':
                if self.mao_jogador_1[1]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mao_jogador_1[1])
                    self.mao_jogador_1[1]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
            elif self.pergunta=='3':
                if self.mao_jogador_1[2]==-1:
                    print("Essa carta ja foi jogada, tente jogar outra carta")
                else:
                    self.mesa.append(self.mao_jogador_1[2])
                    self.mao_jogador_1[2]=-1
                    self.troca_jogador()
                    print(self.mesa)
                    return
        
    def limpa_jogadas(self):
        self.mesa=[]
        return
        
    def verifica_ganhador(self):
        if self.jogador == 0: 
            if self.rodada==1:
                if self.dic_baralho[self.mesa[0]]>self.dic_baralho[self.mesa[1]]: 
                    self.ponto_rodada_jogador_0+=1
                    self.rodada = 2
                    return
                elif self.dic_baralho[self.mesa[0]]<self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_1+=1
                    self.rodada = 2
                    return
                elif self.dic_baralho[self.mesa[0]] == self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_0+=1
                    self.ponto_rodada_jogador_1+=1
                    self.rodada += 1    

            if self.rodada == 2:
                if self.dic_baralho[self.mesa[0]]>self.dic_baralho[self.mesa[1]]: 
                    self.ponto_rodada_jogador_0+=1
                    self.rodada = 3
                    return
                elif self.dic_baralho[self.mesa[0]]<self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_1+=1
                    self.rodada = 3
                    return
                elif self.dic_baralho[self.mesa[0]] == self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_0+=1
                    self.ponto_rodada_jogador_1+=1
                    self.rodada = 3 

            if self.rodada == 3:
                if self.dic_baralho[self.mesa[0]]>self.dic_baralho[self.mesa[1]]: 
                    self.ponto_rodada_jogador_0+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]]<self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_1+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]] == self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_0+=1
                    self.ponto_rodada_jogador_1+=1
                    self.rodada += 1   


        if self.jogador == 1: 
            if self.rodada==1:
                if self.dic_baralho[self.mesa[0]]>self.dic_baralho[self.mesa[1]]: 
                    self.ponto_rodada_jogador_1+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]]<self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_0+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]] == self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_1+=1
                    self.ponto_rodada_jogador_0+=1
                    self.rodada += 1   

            if self.rodada == 2:
                if self.dic_baralho[self.mesa[0]]>self.dic_baralho[self.mesa[1]]: 
                    self.ponto_rodada_jogador_1+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]]<self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_0+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]] == self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_1+=1
                    self.ponto_rodada_jogador_0+=1
                    self.rodada += 1

            if self.rodada == 3:
                if self.dic_baralho[self.mesa[0]]>self.dic_baralho[self.mesa[1]]: 
                    self.ponto_rodada_jogador_1+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]]<self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_0+=1
                    self.rodada+=1
                    return
                elif self.dic_baralho[self.mesa[0]] == self.dic_baralho[self.mesa[1]]:
                    self.troca_jogador()
                    self.ponto_rodada_jogador_1+=1
                    self.ponto_rodada_jogador_0+=1
                    self.rodada += 1



    def fim_rodada(self):

        if self.ponto_rodada_jogador_0 >= 2:
            print('Jogador 0 ganhou a rodada!')
            print()
            self.ponto_jogo_jogador_0 += self.valor_partida
            print('Pontos na partida jogador 0:',self.ponto_jogo_jogador_0)
            print('Pontos na partida jogador 1:',self.ponto_jogo_jogador_1)
            self.rodada = 4
            self.mao_jogador_0=[]
            self.mao_jogador_1=[]
            self.mesa=[]
            self.ponto_rodada_jogador_0=0
            self.ponto_rodada_jogador_1=0   
            self.valor_partida=1
            self.truco = False
            self.reset()
            

        if self.ponto_rodada_jogador_1 >= 2:
            print('Jogador 1 ganhou a rodada!')
            print()
            self.ponto_jogo_jogador_1 += self.valor_partida
            print('Pontos na partida jogador 1:',self.ponto_jogo_jogador_1)
            print('Pontos na partida jogador 0:',self.ponto_jogo_jogador_0)
            self.rodada = 4
            self.ponto_rodada_jogador_0=0
            self.ponto_rodada_jogador_1=0   
            self.valor_partida=1
            self.truco = False
            self.reset()



    def correr_truco(self):
        if self.jogador == 0:
            self.ponto_jogo_jogador_1 += self.valor_partida          
            print(self.ponto_jogo_jogador_0, self.ponto_jogo_jogador_1)
            
            
        elif self.jogador == 1:
            self.ponto_jogo_jogador_0 += self.valor_partida
            print(self.ponto_jogo_jogador_0,self.ponto_jogo_jogador_1)

             
    def reset(self):
        self.mao_jogador_0=[]
        self.mao_jogador_1=[]
        self.mesa=[]
        self.rodada = 1
        self.ponto_rodada_jogador_0=0
        self.ponto_rodada_jogador_1=0   
        self.valor_partida=1
        self.truco = False
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
            
        
        
    def verifica_ganhador_partida(self):
        if self.ponto_jogo_jogador_0>=12:
            return print("Jogador 1 ganhou de {0} a {1}".format(self.ponto_jogo_jogador_0,self.ponto_jogo_jogador_1))
        elif self.ponto_jogo_jogador_1>=12:
            return print("Jogador 2 ganhou de {0} a {1}".format(self.ponto_jogo_jogador_1,self.ponto_jogo_jogador_0))
        else:
            return -1
    
    def cair_truco(self):
        self.valor_partida = 3  
            
    def cair_seis(self):
        self.valor_partida = 6
        
    def cair_nove(self):
        self.valor_partida = 9
        
    def cair_doze(self):
        self.valor_partida = 12
     

