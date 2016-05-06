# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:06:01 2016

@author: moreira
"""


import random



baralho = ['Quatro_ouros','Quatro_espadas','Quatro_copas','Quatro_paus','Cinco_ouros','Cinco_espadas','Cinco_copas','Cinco_paus','Seis_ouros','Seis_espadas','Seis_copas','Seis_paus','Sete_ouros','Sete_espadas','Sete_copas','Sete_paus','Dama_ouros','Dama_espadas','Dama_copas','Dama_paus','Valete_ouros','Valete_espadas','Valete_copas','Valete_paus','Rei_ouros','Rei_espadas','Rei_copas','Rei_paus','As_ouros','As_espadas','As_copas','As_paus','Dois_ouros','Dois_espadas','Dois_copas','Dois_paus','Tres_ouros','Tres_espadas','Tres_copas','Tres_paus']



vira = random.randint(0,39)

    

print(baralho[vira])
    
def manilha(baralho,vira):
    dic_baralho = {'Quatro_ouros':1,'Quatro_espadas':1,'Quatro_copas':1,'Quatro_paus':1,'Cinco_ouros':2,'Cinco_espadas':2,'Cinco_copas':2,'Cinco_paus':2,'Seis_ouros':3,'Seis_espadas':3,'Seis_copas':3,'Seis_paus':3,'Sete_ouros':4,'Sete_espadas':4,'Sete_copas':4,'Sete_paus':4,'Dama_ouros':5,'Dama_espadas':5,'Dama_copas':5,'Dama_paus':5,'Valete_ouros':6,'Valete_espadas':6,'Valete_copas':6,'Valete_paus':6,'Rei_ouros':7,'Rei_espadas':7,'Rei_copas':7,'Rei_paus':7,'As_ouros':8,'As_espadas':8,'As_copas':8,'As_paus':8,'Dois_ouros':9,'Dois_espadas':9,'Dois_copas':9,'Dois_paus':9,'Tres_ouros':10,'Tres_espadas':10,'Tres_copas':10,'Tres_paus':10}
#definindo as manilhas
    vira_carta=baralho[vira]
    a = vira_carta.split('_')
    b = a[1]
    #SE a vira for 3 fiz esse código para não dar erro
    if vira in (36,37,38,39):
        pika = baralho[0]
        espadilha = baralho[1]
        copa = baralho[2]
        zap = baralho[3]
    else:
        if b == 'ouros':
            pika = baralho[vira+4]
            espadilha = baralho[vira+5]
            copa = baralho[vira+6]
            zap = baralho[vira+7]
        
        if b == 'espadas':
            pika = baralho[vira+3]
            espadilha = baralho[vira+4]
            copa = baralho[vira+5]
            zap = baralho[vira+6]
        
        if b == 'copas':
            pika = baralho[vira+2]
            espadilha = baralho[vira+3]
            copa = baralho[vira+4]
            zap = baralho[vira+5]
        
        if b == 'paus':
            pika = baralho[vira+1]
            espadilha = baralho[vira+2]
            copa = baralho[vira+3]
            zap = baralho[vira+4]
        
        
    
#Mudando os valores do dicionário        
    
    print(pika)
    print(espadilha)
    print(copa)
    print(zap)
    dic_baralho[pika]=11
    dic_baralho[espadilha]=12
    dic_baralho[copa]=13
    dic_baralho[zap]=14
    return dic_baralho
    
print(manilha(baralho,vira))
    
    
        


def distribuir_cartas(baralho,vira):
    cartas_dadasA=[]
    cartas_dadasB=[]
    del baralho[vira]
    for i in range(3):
        entregaA = random.randint(0,len(baralho)-1)
        cartas_dadasA.append(baralho[entregaA])
        del baralho[entregaA]
    for t in range(3):
        entregaB = random.randint(0,len(baralho)-1)
        cartas_dadasB.append(baralho[entregaB])
        del baralho[entregaB]
    return cartas_dadasA, cartas_dadasB
    
print(distribuir_cartas(baralho,vira))
        
        
        
        
   
        
        
