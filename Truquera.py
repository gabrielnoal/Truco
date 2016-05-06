# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:06:01 2016

@author: moreira
"""


 
import random


class Algoritmo:
    
    def __init_(self):
        self.baralho = ['Quatro_ouros','Quatro_espadas','Quatro_copas','Quatro_paus','Cinco_ouros','Cinco_espadas','Cinco_copas','Cinco_paus','Seis_ouros','Seis_espadas','Seis_copas','Seis_paus','Sete_ouros','Sete_espadas','Sete_copas','Sete_paus','Dama_ouros','Dama_espadas','Dama_copas','Dama_paus','Valete_ouros','Valete_espadas','Valete_copas','Valete_paus','Rei_ouros','Rei_espadas','Rei_copas','Rei_paus','As_ouros','As_espadas','As_copas','As_paus','Dois_ouros','Dois_espadas','Dois_copas','Dois_paus','Tres_ouros','Tres_espadas','Tres_copas','Tres_paus']
        self.jogador = 0
        self.rodadas = 0
        self.vira = random.randint(0,39)
        self.cartas_dadasA=[]
        self.cartas_dadasB=[]
        self.cartas_jogadasA = []
        self.cartas_jogadasB = []
        
        
   
        
    def manilha(self):
        dic_baralho = {'Quatro_ouros':1,'Quatro_espadas':1,'Quatro_copas':1,'Quatro_paus':1,'Cinco_ouros':2,'Cinco_espadas':2,'Cinco_copas':2,'Cinco_paus':2,'Seis_ouros':3,'Seis_espadas':3,'Seis_copas':3,'Seis_paus':3,'Sete_ouros':4,'Sete_espadas':4,'Sete_copas':4,'Sete_paus':4,'Dama_ouros':5,'Dama_espadas':5,'Dama_copas':5,'Dama_paus':5,'Valete_ouros':6,'Valete_espadas':6,'Valete_copas':6,'Valete_paus':6,'Rei_ouros':7,'Rei_espadas':7,'Rei_copas':7,'Rei_paus':7,'As_ouros':8,'As_espadas':8,'As_copas':8,'As_paus':8,'Dois_ouros':9,'Dois_espadas':9,'Dois_copas':9,'Dois_paus':9,'Tres_ouros':10,'Tres_espadas':10,'Tres_copas':10,'Tres_paus':10}
        #definindo as manilhas
        vira_carta=self.baralho[self.vira]
        a = vira_carta.split('_')
        b = a[1]
        #SE a vira for 3 fiz esse código para não dar erro
        if self.vira in (36,37,38,39):
            pika = self.baralho[0]
            espadilha = self.baralho[1]
            copa = self.baralho[2]
            zap = self.baralho[3]
        else:
            if b == 'ouros':
                pika = self.baralho[self.vira+4]
                espadilha = self.baralho[self.vira+5]
                copa = self.baralho[self.vira+6]
                zap = self.baralho[self.vira+7]
                
            if b == 'espadas':
                pika = self.baralho[self.vira+3]
                espadilha = self.baralho[self.vira+4]
                copa = self.baralho[self.vira+5]
                zap = self.baralho[self.vira+6]
                            
            if b == 'copas':
                pika = self.baralho[self.vira+2]
                espadilha = self.baralho[self.vira+3]
                copa = self.baralho[self.vira+4]
                zap = self.baralho[self.vira+5]
        
            if b == 'paus':
                pika = self.baralho[self.vira+1]
                espadilha = self.baralho[self.vira+2]
                copa = self.baralho[self.vira+3]
                zap = self.baralho[self.vira+4]
                
        
    
#Mudando os valores do dicionário        
    
        dic_baralho[pika]=11
        dic_baralho[espadilha]=12
        dic_baralho[copa]=13
        dic_baralho[zap]=14
        return dic_baralho
    
    
    
        


    def distribuir_cartas(self):
        del self.baralho[self.vira]
        for i in range(3):
            entregaA = random.randint(0,len(self.baralho)-1)
            self.cartas_dadasA.append(self.baralho[entregaA])
            del self.baralho[entregaA]
        for t in range(3):
            entregaB = random.randint(0,len(self.baralho)-1)
            self.cartas_dadasB.append(self.baralho[entregaB])
            del self.baralho[entregaB]
        return self.cartas_dadasA, self.cartas_dadasB  #Lista dentro de lista. Criar 3 listas
    
        
        


    def define_jogador(self):
        if self.jogador == 1:
            self.jogador = 0
        else:
            self.jogador = 1   
        





    def joga(self):
        if self.jogador==0:
            for i in range(3):
                joga = int(input('Qual carta deseja jogar:'))
                if joga == 1:
                    self.cartas_jogadasA.append(self.cartas_dadasA[0])
                    del self.cartas_dadasA[0]
                    print(self.cartas_jogadasA)
                elif joga == 2:
                    self.cartas_jogadasA.append(self.cartas_dadasA[1])
                    del self.cartas_dadasA[1]
                    print(self.cartas_dadasA)
                elif joga == 3:
                    self.cartas_jogadasA.append(self.cartas_dadasA[2])
                    del self.cartas_dadasA[2]
                    print(self.cartas_dadasA)
                    print(self.cartas_jogadasA)
          
        elif self.jogador==1:
              for i in range(3):
                  joga = int(input('Qual carta deseja jogar:'))
                  if joga == 1:
                      self.cartas_jogadasB.append(self.cartas_dadasB[0])
                      del self.cartas_dadasB[0]
                      
                  elif joga == 2:
                      self.cartas_jogadasB.append(self.cartas_dadasB[1])
                      del self.cartas_dadasB[1]
                      
                  elif joga == 3:
                      self.cartas_jogadasB.append(self.cartas_dadasB[2])
                      del self.cartas_dadasB[2]
                      
                      



        
        
        
   
        
        
