# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 07:59:47 2015

@author: carolinapiu
"""
import random
#abre o arquivo dos barcos
barcos = open("barcos.csv", "r+")
barcos1 = barcos.readlines()
#print (barcos1)
a = barcos1[0].split(',')
b = barcos1[1].split(',')
c = barcos1[2].split(',')
d = barcos1[3].split(',')
e = barcos1[4].split(',')

#matriz que vai ficar aparente para o jogador como a matriz do oponente
matriza = []
for x in range(10):
    matriza.append(["O"] * 10)
#print (matriza)

def matriz_aparente(matriza):
    for linha in matriza:
        print (" ".join(linha))
                  
 #regras do jogo          
print ("REGRAS DO JOGO:\n\nArmas dispniveis:\n 1 porta aviões (ocupa 5 casas)\n 1 navio de guerra (ocupa 4 casas)\n 1 cruzeiro (ocupa 3 casas)\n 1 submarino (ocupa 2 casas)\n 1 destruidor(ocupa 1 casa)\n\nPreparação do jogo:\n   Você deve distribuir todos os seus barcos pelo tabuleiro podendo ser na vertical ou horizontal, sem que um fique em cima do outro, estando todos completamente dentro do tabuleiro.\n\nJogando:\n   Você deve escolher uma linha e uma coluna nas quais irá atirar uma bomba a cada jogada. Se no tabuleiro aparecer um 'A', sinto muito, mas você acertou a aguá, se aparecer um 'B', muito bem, você acertou parte de um barco. No jogo contra o computador ganha quem fizer 15 pontos primeiro, ou seja destruir todas as partes de todos os barcos.\n\n    QUE A BATALHA COMEÇE, BOA SORTE!\n ")
 # definição do que é cada barco
porta_avioes = a[1: 6]
navio_de_guerra = b[1: 5]
cruzeiro = c[1:4]
submarino = d[1:3]
destruidor = e[1:2]

barco = []
barco.append(porta_avioes)
barco.append(navio_de_guerra)
barco.append(cruzeiro)
barco.append(submarino)
barco.append(destruidor)

#print (barco)

#matriz onde o jogador coloca os seus barcos
matrizj = []
for x in range(10):
    matrizj.append(["O"] * 10)
#print (matrizj)

def matriz_jogador(matrizj):
    for linha in matrizj:
        print (" ".join(linha))


#matriz que não aparece para o jogador, mas os barcos estão nela
matrize = []
for x in range(10):
    matrize.append(["O"] * 10)
#print (matrize)

def matriz_escondida(matrize):
    for linha in matrize:
        print (" ".join(linha))
    
#escolha do local dos barcos das pessoas
#porta avioes
linha_porta = int(input("Escreva a linha onde ficara a ponta do seu porta aviões: "))
while linha_porta not in range(10): #para ver se jogador escreveu um numero valido
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        linha_porta = int(input("Escreva a linha onde ficara a ponta do seu porta aviões: "))
coluna_porta = int(input("Escreva a coluna onde ficara a ponta do seu porta aviões: "))
while coluna_porta not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        coluna_porta = int(input("Escreva a coluna onde ficara a ponta do seu porta aviões: "))
ps1 = str(input("Escreva (h) se quiser que seu porta aviões fique na horizontal ou (v) se quiser na vertical: " ))
ps = ps1.lower()
if ps1 == "h":
    while coluna_porta>4:
        print("Seu porta aviões está para fora da matriz, escolha outro local:")
        linha_porta = int(input("Escreva a novamente linha onde ficara a ponta do seu porta aviões: "))
        while linha_porta not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            linha_porta = int(input("Escreva a linha onde ficara a ponta do seu porta aviões: "))
        coluna_porta = int(input("Escreva a novamente coluna onde ficara a ponta do seu porta aviões: "))
        while coluna_porta not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        coluna_porta = int(input("Escreva a coluna onde ficara a ponta do seu porta aviões: "))
        ps1 = str(input("Escreva novamente (h) se quiser que seu porta aviões fique na horizontal ou (v) se quiser na vertical: " ))
        ps = ps1.lower()
if ps1=="v":
    while linha_porta>4:
       print("Seu porta aviões está para fora da matriz, escolha outro local:")
       linha_porta = int(input("Escreva a novamente linha onde ficara a ponta do seu porta aviões: "))
       while linha_porta not in range(10):
           print ("Você tem certeza de que escreveu um número entre 0 e 9?")
           linha_porta = int(input("Escreva a linha onde ficara a ponta do seu porta aviões: "))
       coluna_porta = int(input("Escreva a novamente coluna onde ficara a ponta do seu porta aviões: "))
       while coluna_porta not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
       coluna_porta = int(input("Escreva a coluna onde ficara a ponta do seu porta aviões: "))
       ps1 = str(input("Escreva novamente (h) se quiser que seu porta aviões fique na horizontal ou (v) se quiser na vertical: " ))
       ps = ps1.lower()
'''

while ps != 'h' or ps != 'v': #para ver se jogador escreveu uma letra valida
    print("Você tem certeza de que escreveu 'h' para 'horizontal'ou 'v' para 'vertical'?")
    ps1 = str(input("Escreva (h) se quiser que seu porta aviões fique na horizontal ou (v) se quiser na vertical: " ))
    ps = ps1.lower()
'''  

#colocando o porta avioes do jogador
if ps == 'h':
    matrizj[linha_porta][coluna_porta]="B"
    matrizj[linha_porta][coluna_porta+1]="B"
    matrizj[linha_porta][coluna_porta+2]="B"
    matrizj[linha_porta][coluna_porta+3]="B"
    matrizj[linha_porta][coluna_porta+4]="B"
if ps == "v":
    matrizj[linha_porta][coluna_porta]="B"
    matrizj[linha_porta+1][coluna_porta]="B"
    matrizj[linha_porta+2][coluna_porta]="B"
    matrizj[linha_porta+3][coluna_porta]="B"
    matrizj[linha_porta+4][coluna_porta]="B"
print (matrizj)

#navio de guerra
linha_navio = int(input("Escreva a linha onde ficara a ponta do seu navio de guerra: "))
while linha_navio not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        linha_navio = int(input("Escreva a linha onde ficara a ponta do seu navio de guerra: "))
coluna_navio = int(input("Escreva a coluna onde ficara a ponta do seu navio de guerra: "))
while coluna_navio not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        coluna_navio = int(input("Escreva a coluna onde ficara a ponta do seu navio de guerra: "))
ns1 = input("Escreva (h) se quiser que seu navio de guerra fique na horizontal ou (v) se quiser na vertical: " )
ns = ns1.lower()
if ns1 == "h":
    while coluna_navio>5:
        print("Seu navio de guerra está para fora da matriz, escolha outro local:")
        linha_navio = int(input("Escreva a novamente linha onde ficara a ponta do seu navio de guerra: "))
        while linha_navio not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            linha_navio = int(input("Escreva a linha onde ficara a ponta do seu navio de guerra: "))
        coluna_navio = int(input("Escreva a novamente coluna onde ficara a ponta do seu navio de guerra: "))
        while coluna_navio not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        coluna_navio = int(input("Escreva a coluna onde ficara a ponta do seu navio de guerra: "))
        ns1 = str(input("Escreva novamente (h) se quiser que seu navio de guerra fique na horizontal ou (v) se quiser na vertical: " ))
        ns = ns1.lower()
if ns1=="v":
    while linha_navio>5:
        print("Seu navio de guerra está para fora da matriz, escolha outro local:")
        linha_navio = int(input("Escreva a novamente linha onde ficara a ponta do seu navio de guerra: "))
        while linha_navio not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            linha_navio = int(input("Escreva a linha onde ficara a ponta do seu navio de guerra: "))
        coluna_navio = int(input("Escreva a novamente coluna onde ficara a ponta do seu navio de guerra: "))
        while coluna_navio not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            coluna_navio = int(input("Escreva a coluna onde ficara a ponta do seu navio de guerra: "))
        ns1 = str(input("Escreva novamente (h) se quiser que seu navio de guerra fique na horizontal ou (v) se quiser na vertical: " ))
        ns = ns1.lower()
'''

while ns!="h" or ns!="v":
    print("Você tem certeza de que escreveu 'h' para 'horizontal'ou 'v' para 'vertical'?")
    ns1 = input("Escreva (h) se quiser que seu navio de guerra fique na horizontal ou (v) se quiser na vertical: " )
    ns = ns1.lower()
'''

#colocando o navio de guerra do jogador
if ns == "h":
    matrizj[linha_navio][coluna_navio]="B"
    matrizj[linha_navio][coluna_navio+1]="B"
    matrizj[linha_navio][coluna_navio+2]="B"
    matrizj[linha_navio][coluna_navio+3]="B"
if ns == "v":
    matrizj[linha_navio][coluna_navio]="B"
    matrizj[linha_navio+1][coluna_navio]="B"
    matrizj[linha_navio+2][coluna_navio]="B"
    matrizj[linha_navio+3][coluna_navio]="B"
print (matrizj)

#cruzeiro
linha_cruzeiro = int(input("Escreva a linha onde ficara a ponta do seu cruzeiro: "))
while linha_cruzeiro not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        linha_cruzeiro = int(input("Escreva a linha onde ficara a ponta do seu cruzeiro: "))
coluna_cruzeiro = int(input("Escreva a coluna onde ficara a ponta do seu cruzeiro: "))
while coluna_cruzeiro not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        coluna_cruzeiro = int(input("Escreva a coluna onde ficara a ponta do seu cruzeiro: "))
cs1 = input("Escreva (h) se quiser que seu cruzeiro fique na horizontal ou (v) se quiser na vertical: " )
cs = cs1.lower()
if cs1 == "h":
    while coluna_cruzeiro>6:
        print("Seu cruzeiro está para fora da matriz, escolha outro local:")
        linha_cruzeiro = int(input("Escreva a novamente linha onde ficara a ponta do seu cruzeiro: "))
        while linha_cruzeiro not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            linha_cruzeiro = int(input("Escreva a linha onde ficara a ponta do seu cruzeiro: "))
        coluna_cruzeiro = int(input("Escreva a novamente coluna onde ficara a ponta do seu cruzeiro: "))
        while coluna_cruzeiro not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            coluna_cruzeiro = int(input("Escreva a coluna onde ficara a ponta do seu cruzeiro: "))
        cs1 = str(input("Escreva novamente (h) se quiser que seu cruzeiro fique na horizontal ou (v) se quiser na vertical: " ))
        cs = cs1.lower()
if ns1=="v":
    while linha_cruzeiro>6:
        print("Seu cruzeiro está para fora da matriz, escolha outro local:")
        linha_cruzeiro = int(input("Escreva a novamente linha onde ficara a ponta do seu cruzeiro: "))
        while linha_cruzeiro not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            linha_cruzeiro = int(input("Escreva a linha onde ficara a ponta do seu cruzeiro: "))
        coluna_cruzeiro = int(input("Escreva a novamente coluna onde ficara a ponta do seu cruzeiro: "))
        while coluna_cruzeiro not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            coluna_cruzeiro = int(input("Escreva a coluna onde ficara a ponta do seu cruzeiro: "))
        cs1 = str(input("Escreva novamente (h) se quiser que seu navio de guerra fique na horizontal ou (v) se quiser na vertical: " ))
        cs = cs1.lower()

'''
while cs!="h" or cs!="v":
    print("Você tem certeza de que escreveu 'h' para 'horizontal'ou 'v' para 'vertical'?")
    cs1 = input("Escreva (h) se quiser que seu cruzeiro fique na horizontal ou (v) se quiser na vertical: " )
    cs = cs1.lower()
'''

#colocando o cruzeiro do jogador
if cs == "h":
    matrizj[linha_cruzeiro][coluna_cruzeiro]="B"
    matrizj[linha_cruzeiro][coluna_cruzeiro+1]="B"
    matrizj[linha_cruzeiro][coluna_cruzeiro+2]="B"
if cs == "v":
    matrizj[linha_cruzeiro][coluna_cruzeiro]="B"
    matrizj[linha_cruzeiro+1][coluna_cruzeiro]="B"
    matrizj[linha_cruzeiro+2][coluna_cruzeiro]="B"  
print(matrizj)

#submarino
linha_submarino = int(input("Escreva a linha onde ficara a ponta do seu submarino: "))
while linha_submarino not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        linha_submarino = int(input("Escreva a linha onde ficara a ponta do seu submarino: "))
coluna_submarino = int(input("Escreva a coluna onde ficara a ponta do seu submarino: "))
while coluna_submarino not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        coluna_submarino = int(input("Escreva a coluna onde ficara a ponta do seu submarino: "))
ss1 = input("Escreva (h) se quiser que seu submarino fique na horizontal ou (v) se quiser na vertical: " )
ss = ss1.lower()
if ss1 == "h":
    while coluna_submarino>7:
        print("Seu submarino está para fora da matriz, escolha outro local:")
        linha_submarino = int(input("Escreva a novamente linha onde ficara a ponta do seu submarino: "))
        while linha_submarino not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            linha_submarino = int(input("Escreva a linha onde ficara a ponta do seu submarino: "))
        coluna_submarino = int(input("Escreva a novamente coluna onde ficara a ponta do seu submarino: "))
        while coluna_submarino not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            coluna_submarino = int(input("Escreva a coluna onde ficara a ponta do seu submarino: "))
        ss1 = str(input("Escreva novamente (h) se quiser que seu submarino fique na horizontal ou (v) se quiser na vertical: " ))
        ss = ss1.lower()
if ns1=="v":
    while linha_submarino>7:
        print("Seu submarino está para fora da matriz, escolha outro local:")
        linha_submarino = int(input("Escreva a novamente linha onde ficara a ponta do seu submarino: "))
        while linha_submarino not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            linha_submarino = int(input("Escreva a linha onde ficara a ponta do seu submarino: "))
        coluna_submarino = int(input("Escreva a novamente coluna onde ficara a ponta do seu submarino: "))
        while coluna_submarino not in range(10):
            print ("Você tem certeza de que escreveu um número entre 0 e 9?")
            coluna_submarino = int(input("Escreva a coluna onde ficara a ponta do seu submarino: "))
        ss1 = str(input("Escreva novamente (h) se quiser que seu submarino fique na horizontal ou (v) se quiser na vertical: " ))
        ss = ss1.lower()

'''
while ss!="h" or ss!="v":
    print("Você tem certeza de que escreveu 'h' para 'horizontal'ou 'v' para 'vertical'?")
    ss1 = input("Escreva (h) se quiser que seu submarino fique na horizontal ou (v) se quiser na vertical: " )
    ss = ss1.lower()
'''

#colocando o submarino do jogador
if ss == "h":
    matrizj[linha_submarino][coluna_submarino]="B"
    matrizj[linha_submarino][coluna_submarino+1]="B"
if ss == "v":
    matrizj[linha_submarino][coluna_submarino]="B"
    matrizj[linha_submarino+1][coluna_submarino]="B"
print(matrizj)

#destruidor
linha_destruidor = int(input("Escreva a linha onde ficara a ponta do seu destruidor: "))
while linha_destruidor not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        linha_destruidor = int(input("Escreva a linha onde ficara a ponta do seu destruidor: "))
coluna_destruidor = int(input("Escreva a linha onde ficara a ponta do seu destruidor: "))
while coluna_destruidor not in range(10):
        print ("Você tem certeza de que escreveu um número entre 0 e 9?")
        coluna_destruidor = int(input("Escreva a coluna onde ficara a ponta do seu destruidor: "))
#colocando o destruidor do jogador
matrizj[linha_destruidor][coluna_destruidor] = "B"
print ("Os seus barcos ficaram assim no tabuleiro:\n",matrizj)

#local onde cada barco será colocado na matrize:
lista = list(range(10))
#print (lista)
col1=random.choice(lista)
lin1 = random.choice(lista)
col2=random.choice(lista)
lin2 = random.choice(lista)
col3=random.choice(lista)
lin3 = random.choice(lista)
col4=random.choice(lista)
lin4 = random.choice(lista)
col5=random.choice(lista)
lin5 = random.choice(lista)
sentido=['h', 'v']
sen1 = random.choice(sentido) #sentido do submarino
sen2 = random.choice(sentido) #sentido do cruzeiro
sen3 = random.choice(sentido) #sentido do navio de guerra
sen4 = random.choice(sentido) #sentido do porta avioes

#colocando o destruidor
matrize[lin1][col1] = "B"

#colocando o submarino   
if sen1 == 'h':
    while col2 > 7: #impede que o barco passe da matriz
            col2=random.choice(lista)
    while matrize[lin2][col2]=="B" or matrize[lin2][col2+1]=="B": #impede que um barco fique em cima do outro
        col2=random.choice(lista)
        lin2 = random.choice(lista)
        while col2 > 7:
            col2=random.choice(lista)
    matrize[lin2][col2]="B"
    matrize[lin2][col2+1]="B"
if sen1 == 'v':
    while lin2>7:
            lin2 = random.choice(lista)
    while matrize[lin2][col2]=="B" or matrize[lin2+1][col2]=="B":
        col2=random.choice(lista)
        lin2 = random.choice(lista)
        while lin2>7:
            lin2 = random.choice(lista)
    matrize[lin2][col2]="B"
    matrize[lin2+1][col2]="B"
#colocando o cruzeiro
if sen2 == "h":
    while col3 > 6:
        col3=random.choice(lista)
    while matrize[lin3][col3]=="B" or matrize[lin3][col3+1]=="B" or matrize[lin3][col3+2]=="B":
        col3=random.choice(lista)
        lin3=random.choice(lista)
        while col3 > 6:
            col3=random.choice(lista)
    matrize[lin3][col3]="B"
    matrize[lin3][col3+1]="B"
    matrize[lin3][col3+2]="B"
if sen2 == "v":
    while lin3>6:
        lin3 = random.choice(lista)
    while matrize[lin3][col3]=="B" or matrize[lin3+1][col3]=="B" or matrize[lin3+2][col3]=="B":
        col3=random.choice(lista)
        lin3=random.choice(lista)
        while col3 > 6:
            col3=random.choice(lista)
    matrize[lin3][col3]="B"
    matrize[lin3+1][col3]="B"
    matrize[lin3+2][col3]="B"
    
#colocando o navio de guerra
if sen3 == "h":
    while col4 > 5:
            col4=random.choice(lista)
    while matrize[lin4][col4]=="B" or  matrize[lin4][col4+1]=="B" or matrize[lin4][col4+2]=="B" or matrize[lin4][col4+3]=="B":
        col4=random.choice(lista)
        lin4=random.choice(lista)        
        while col4 > 5:
            col4=random.choice(lista)
    matrize[lin4][col4]="B"
    matrize[lin4][col4+1]="B"
    matrize[lin4][col4+2]="B"
    matrize[lin4][col4+3]="B"
if sen3 == "v":
    while lin4>5:
        lin4 = random.choice(lista)
    while matrize[lin4][col4]=="B" or matrize[lin4+1][col4]=="B" or matrize[lin4+2][col4]=="B" or matrize[lin4+3][col4]=="B":
        col4=random.choice(lista)
        lin4=random.choice(lista)         
        while lin4>5:
             lin4 = random.choice(lista)
    matrize[lin4][col4]="B"
    matrize[lin4+1][col4]="B"
    matrize[lin4+2][col4]="B"
    matrize[lin4+3][col4]="B"
#colocando o porta avioes
if sen4 == "h":
    while col5 > 4:
            col5=random.choice(lista)
    while matrize[lin5][col5]=="B" or matrize[lin5][col5+1]=="B" or matrize[lin5][col5+2]=="B" or matrize[lin5][col5+3]=="B" or matrize[lin5][col5+4]=="B":
        col5=random.choice(lista)
        lin5=random.choice(lista)
        while col5 > 4:
            col5=random.choice(lista)
    matrize[lin5][col5]="B"
    matrize[lin5][col5+1]="B"
    matrize[lin5][col5+2]="B"
    matrize[lin5][col5+3]="B"
    matrize[lin5][col5+4]="B"
if sen4 == "v":
    while lin5>4:
        lin5 = random.choice(lista)
    while matrize[lin5][col5]=="B" or  matrize[lin5+1][col5]=="B" or matrize[lin5+2][col5]=="B" or matrize[lin5+3][col5]=="B" or matrize[lin5+4][col5]=="B":
        col5=random.choice(lista)
        lin5=random.choice(lista)
        while lin5>4:
            lin5 = random.choice(lista)
    matrize[lin5][col5]="B"
    matrize[lin5+1][col5]="B"
    matrize[lin5+2][col5]="B"
    matrize[lin5+3][col5]="B"
    matrize[lin5+4][col5]="B"
    
print (matrize)
matrize2=matrizj
#print(matrize2)

print("Agora que seu campo de batalha já esta pronto vamos começar a jogar!")
pontos_jogador = 0
pontos_computador = 0
while pontos_jogador !=15 or pontos_computador!=15:
    print ("PLACAR:")
    print("Seus pontos: ", pontos_jogador)
    print("Pontos do computador:", pontos_computador)
    #print("Seu tabuleiro:", matrizj)
    print("Tabuleiro do computador: \n", matriza)
    chute_linha = int(input("Digite uma linha para jogar sua bomba: ")) #chute da linha do jogador
    while chute_linha not in range(10): #para que esteja entre 0 e 9 
        print("Você deve escrever um número de 0 a 9")
        chute_linha = int(input("Digite uma novamente linha para jogar sua bomba: "))
    chute_coluna = int(input("Digite uma coluna para jogar sua bomba: ")) #chute da coluna do jogador
    while chute_coluna not in range(10): #para que esteja entre 0 e 9
        print("Você deve escrever um número de 0 a 9")
        chute_coluna = int(input("Digite novamente uma coluna para jogar sua bomba: "))
    while matrize[chute_linha][chute_coluna]=="1": #para que a pessoa nao atire duas vezes no mesmo local
        print("Você ja atirou nesse local, escolha outro")
        chute_linha = int(input("Digite novamente uma linha para jogar sua bomba: "))
        while chute_linha not in range(10): #para que esteja entre 0 e 9 
            print("Você deve escrever um número de 0 a 9")
            chute_linha = int(input("Digite uma novamente linha para jogar sua bomba: "))
        chute_coluna = int(input("Digite novamente uma coluna para jogar sua bomba: "))
        while chute_coluna not in range(10): #para que esteja entre 0 e 9
            print("Você deve escrever um número de 0 a 9")
            chute_coluna = int(input("Digite novamente uma coluna para jogar sua bomba: "))
    if matrize[chute_linha][chute_coluna] == "B":
        print("Muito bem, você acertou parte de um barco")
        pontos_jogador+=1
        matriza[chute_linha][chute_coluna]="B"
        matrize[chute_linha][chute_coluna]="1"
    if matrize[chute_linha][chute_coluna]== "O":
        print("Dessa vez você não teve tanta sorte, acertou a aguá...")
        matriza[chute_linha][chute_coluna]="A"
        matrize[chute_linha][chute_coluna]="1"
    chutes=list(range(10))
    chute_pc_linha = random.choice(chutes)
    chute_pc_coluna = random.choice(chutes)
    while matrize2[chute_pc_linha][chute_pc_coluna]=="1":
        chute_pc_linha = random.choice(chutes)
        chute_pc_coluna = random.choice(chutes)
    if matrizj[chute_pc_linha][chute_pc_coluna] == "O":
        print ("O computador atirou na água")
        matrize2[chute_pc_linha][chute_pc_coluna]= "1"
        #print (matrize2)
    if matrizj[chute_pc_linha][chute_pc_coluna]=="B":
        print("O computador acertou parte de um dos seus barcos na linha ", chute_pc_linha, "e na coluna ", chute_pc_coluna)
        pontos_computador+=1  
        matrize2[chute_pc_linha][chute_pc_coluna]="1"
        #print (matrize2)
    if pontos_jogador == 15 and pontos_computador <15:
        print("PARABÉNS VOCÊ GANHOU O JOGO")
        break
    if pontos_computador == 15 and pontos_jogador<15:
        print("Não foi dessa vez. Você perdeu... :(")
        break
    if pontos_computador == 15 and pontos_jogador==15:
        print("Foi um empate!")
        break
    
#problemas:
'''
1- se o jogador escrever uma str onde é int o jogo da erro
2- se o jogador nao escrever h ou v onde deve ser escrito ele nao identifica
'''