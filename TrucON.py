    
    
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
#            print(self.baralho)            
            return self.vira
            
            
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
#            print(self.baralho)            
            return self.vira
            
    def distribuir_cartas(self):
        self.carta_1_1 = random.randint(0,38)
        while self.baralho[self.carta_1_1] == "-1":
            self.carta_1_1 = random.randint(0,38)
        self.mao_jogador_0.append(self.baralho[self.carta_1_1]) # Mudar as outras cartas
        self.baralho[self.carta_1_1] = "-1"
        
        self.carta_1_2 = random.randint(0,38)
        while self.baralho[self.carta_1_2] == "-1":
            self.carta_1_2 = random.randint(0,38)          
        self.mao_jogador_0.append(self.baralho[self.carta_1_2])
        self.baralho[self.carta_1_2] = "-1"
        
        self.carta_1_3 = random.randint(0,38)
        while self.baralho[self.carta_1_3] == "-1":
            self.carta_1_3 = random.randint(0,38)
        self.mao_jogador_0.append(self.baralho[self.carta_1_3])
        self.baralho[self.carta_1_3] = "-1"
        
        self.carta_3_1 = random.randint(0,38)
        while self.baralho[self.carta_3_1] == "-1":
            self.carta_3_1 = random.randint(0,38)
        self.mao_jogador_1.append(self.baralho[self.carta_3_1])
        self.baralho[self.carta_3_1] = "-1"
        
        self.carta_3_2 = random.randint(0,38)
        while self.baralho[self.carta_3_2] == "-1":
            self.carta_3_2 = random.randint(0,38)
        self.mao_jogador_1.append(self.baralho[self.carta_3_2])
        self.baralho[self.carta_3_2] = "-1"
        
        self.carta_3_3 = random.randint(0,38)
        while self.baralho[self.carta_3_3] == "-1":
            self.carta_3_3 = random.randint(0,38)          
        self.mao_jogador_1.append(self.baralho[self.carta_3_3])
        self.baralho[self.carta_3_3] = "-1"
        
        print (self.baralho)
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
                    self.rodada = 2   

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
            self.mao_jogador_0=[]
            self.mao_jogador_1=[]
            self.mesa=[]
            self.ponto_rodada_jogador_0=0
            self.ponto_rodada_jogador_1=0   
            self.valor_partida=1
            self.truco = False
            

        if self.ponto_rodada_jogador_1 >= 2:
            print('Jogador 1 ganhou a rodada!')
            print()
            self.ponto_jogo_jogador_1 += self.valor_partida
            print('Pontos na partida jogador 1:',self.ponto_jogo_jogador_1)
            print('Pontos na partida jogador 0:',self.ponto_jogo_jogador_0)
            self.mao_jogador_0=[]
            self.mao_jogador_1=[]
            self.mesa=[]
            self.ponto_rodada_jogador_0=0
            self.ponto_rodada_jogador_1=0   
            self.valor_partida=1
            self.truco = False

            
        
    def placar(self):
        print ("Jogador 1: {0} e Jogador 2: {1}".format(self.ponto_jogo_jogador_0,self.ponto_jogo_jogador_1))
        
    def verifica_ganhador_partida(self):
        if self.ponto_jogo_jogador_0<=12:
            return ("Jogador 1 ganhou de {0} a {1}".format(self.ponto_jogo_jogador_0,self.ponto_jogo_jogador_1))
        elif self.ponto_jogo_jogador_1<=12:
            return ("Jogador 2 ganhou de {0} a {1}".format(self.ponto_jogo_jogador_1,self.ponto_jogo_jogador_0))
        else:
            return -1
    

        
    def pedir_truco(self):
        if self.jogador == 0:
            print("RESPONDA TODAS AS PERGUNTAS EM CARACTERES MINÚSCULO E OS NÚMEROS POR EXTENSO")
            if self.pergunta == 'truco':
                self.truco = True
                print('O outro jogador pediu truco')
                self.resposta = input('Cair no truco, correr ou pedir seis?')
               
                if self.resposta == 'cair':   
                    self.valor_partida = 3 # Atualizou o valor da partida
                elif self.resposta == 'seis' :
                    self.pedir_seis()
                else:
                    self.correr()

        if self.jogador == 1:
            if self.pergunta == 'truco':
                print('O outro jogador pediu truco')
                self.resposta = input('Cair no truco, correr ou pedir seis?')
                if self.resposta == 'cair' :
                    self.valor_partida = 3 # Atualizou o valor da partida
                elif self.resposta == 'seis' or '6':
                    self.pedir_seis()
                else:
                    self.correr()



    def pedir_seis(self):
        if self.jogador == 0:
            if self.pergunta == 'seis':
                self.seis = True
            print('O outro jogador pediu seis')
            self.resposta = input('Cair no seis, correr ou pedir nove?')
            if self.resposta == 'cair' :
                self.valor_partida = 6 # Atualizou o valor da partida
            elif self.resposta == 'nove':
                self.pedir_nove()
            else:
                self.correr()

        if self.jogador == 1:
            if self.resposta == 'seis' :
                self.seis = True
            print('O outro jogador pediu seis')  
            self.resposta = input('Cair no seis, correr ou pedir nove?')
            if self.resposta == 'cair' :
                self.valor_partida = 6 # Atualizou o valor da partida
            elif self.resposta ==  'nove':
                self.pedir_nove()
            else:
                self.correr()
            



    def pedir_nove(self):
        if self.jogador == 0:
            if self.pergunta == 'nove':
                self.nove = True
            print('O outro jogador pediu nove')
            self.resposta = input('Cair no nove, correr ou pedir doze?')
            if self.resposta == 'cair':
                self.valor_partida = 9 # Atualizou o valor da partida
            elif self.resposta == 'doze' or '12':
                self.pedir_doze()
            else:
                self.correr()
        
        if self.jogador == 1:
            if self.pergunta == 'nove' :
                self.nove = True
            print('O outro jogador pediu nove')
            self.resposta = input('Cair no nove, correr ou pedir doze?')
            if self.resposta == 'cair' :
                self.valor_partida = 9 # Atualizou o valor da partida
            elif self.resposta == 'doze' or 'Doze' or '12':
                self.pedir_doze()
            else:
                self.correr()
        

    def pedir_doze(self):
        if self.jogador == 0:
            if self.pergunta == "doze":
                self.doze = True
            print('O outro jogador pediu doze')
            self.resposta = input('Cair no doze ou correr?')
            if self.resposta == 'cair' :
                self.valor_partida = 12 # Atualizou o valor da partida
            else:
                self.correr()
        
        if self.jogador == 1:
            if self.pergunta == "doze":
                self.doze = True
            print('O outro jogador pediu doze')
            self.resposta = input('Cair no doze ou correr?')
            if self.resposta == 'cair' :
                self.valor_partida = 12 # Atualizou o valor da partida
            else:
                self.correr()


    def correr(self):
        if self.jogador == 1:
            self.ponto_jogo_jogador_1 += self.valor_partida
        if self.jogador == 0:
            self.ponto_jogo_jogador_0 += self.valor_partida
        self.fim_rodada()



            

    def gameloop(self):
        self.fim_jogo = False

        self.manilha()
        self.distribuir_cartas()

        print(self.mao_jogador_0,self.mao_jogador_1)
        self.joga_carta()
        self.joga_carta()          
        self.verifica_ganhador()
        self.limpa_jogadas()
        self.verifica_ganhador_partida()       
        print(self.ponto_rodada_jogador_0)
        print(self.ponto_rodada_jogador_1)
        self.fim_rodada()
       
        
        print(self.mao_jogador_0,self.mao_jogador_1)
        self.joga_carta()
        self.joga_carta()        
        self.verifica_ganhador()
        self.limpa_jogadas()
        self.verifica_ganhador_partida()
        print(self.ponto_rodada_jogador_0)
        print(self.ponto_rodada_jogador_1)
        self.fim_rodada()

        print(self.mao_jogador_0,self.mao_jogador_1)
        self.joga_carta()
        self.joga_carta()        
        self.pedir_truco()
        self.verifica_ganhador()
        self.limpa_jogadas()
        self.verifica_ganhador_partida()
        self.fim_rodada()
        


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
#print(jogo.mao_jogador_0,jogo.mao_jogador_1)
#print(jogo.joga_carta())
#print(jogo.joga_carta())
#print(jogo.verifica_ganhador())
#print(jogo.ponto_rodada_jogador_0)
#print(jogo.ponto_rodada_jogador_1)
#
#
#print(jogo.mao_jogador_0,jogo.mao_jogador_1)
#print(jogo.joga_carta())
#print(jogo.joga_carta())
#print(jogo.verifica_ganhador())
#print(jogo.ponto_rodada_jogador_0)
#print(jogo.ponto_rodada_jogador_1)
#
#
#print(jogo.placar())
