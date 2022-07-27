import cv2 as cv
import numpy as np
import time
import os

def showimage(img): #Função que mostra o tabuleiro na tela e não trava esperando o usuário apertar alguma tecla.
    from matplotlib import pyplot as plt  
    plt.imshow(img)
    plt.show(block=False)

def showimage_2(img):#Função que mostra o tabuleiro, porém trava ele na tela até o usuário apertar alguma tecla.
    from matplotlib import pyplot as plt
    plt.imshow(img)
    plt.show()

def drawLine(img, startPoint, endPoint, color, thickness): #Função que desenha uma linha na tela e tem como paramêtros a imagem que você quer fazer a linha e a posição inicial e final da linha.
    cv.line(img, startPoint, endPoint, color, thickness)


def x(img, posx, posy, color = (0, 0, 0), thickness = 2): #Função que desenha um "X" no tabuleiro. O "X" são duas linhas que se cruzam. Então, nessa função eu chamo duas vezes a função de desenhar linha. 
    startposx, startposy = 50 + posx * 80, 100 + posy* 80
    endpointx, endpointy = 90 + posx * 80, 140 + posy* 80
    cv.line(img, (startposx, startposy), (endpointx, endpointy), color, thickness)
    cv.line(img, (endpointx, startposy), (startposx, endpointy), color, thickness)


def drawCircle(img, centerX, centerY, raio = 20, color = (0, 0, 0), thickness = 2): #Função que desenha uma circunferência no tabuleiro
    init_centerX, init_centerY = 71 + centerX * 80, 123 + centerY * 80

    
    cv.circle(img, (init_centerX, init_centerY), raio, color, thickness)


    


def main():
    count = 0
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("                        BEM VINDO AO JOGO DA VELHA                           ")
    j1 = input("Digite o nome do jogador 1: ")
    j2 = input("Digite o nome do jogador 2: ")
    j1 = j1.title()
    j2 = j2.title()
    board = np.empty([400, 300, 3], dtype = np.uint8) #Criação do tabuleiro de tamanho 400x300 e 3 canais de cores. O dtype é "uint8" pois vamos preenchê-lo com inteiros de 0 a 255.
    board.fill(255) #Preenchendo a matriz do tabuleiro com 255 ([255, 255, 255]) pra deixar ele na cor branca.

    person1 = 1
    person2 = 2
    drawLine(board, (100, 100), (100, 300), (0, 0, 0), 3)  #Linhas (51 a 54) - Desenham as linhas do tabuleiro do jogo da velha
    drawLine(board, (200, 100), (200, 300), (0, 0, 0), 3)
    drawLine(board, (50, 250), (250, 250), (0, 0, 0), 3)
    drawLine(board, (50, 150), (250, 150), (0, 0, 0), 3)
    currentMatch = board.copy()
    turn = person1 #O primeiro turno sempre é do jogador 1.
    posicoes_ocupadas = np.array([[0]*3]*3) #Essa é a matriz do jogo da velha. É essa matriz que vai fazer o jogo funcionar. Lembrando que é uma matriz 3x3
    showimage(currentMatch) #Mostrando o tabuleiro antes de pedir as coordenadas.
    while True:
        if turn == person1:
            print(f"VEZ DO JOGADOR: {j1} (X)")
            print('--------------------------------------------------------------------------')
            print('--------------------------------------------------------------------------')
            print("Canto superior esquerdo = (1, 1)" + '\n' + "Canto superior meio = (2, 1)" + '\n' + "Canto superior direito = (3, 1)")
            print("Canto meio esquerdo = (1, 2)" + '\n' + "Meio = (2, 2)" + '\n' + "Canto meio direito = (3, 2)")
            print("Canto inferior esquerdo = (1, 3)" + '\n' "Canto inferior meio = (2, 3)" + '\n' + "Canto inferior direito = (3, 3)")
            print('--------------------------------------------------------------------------')
            print('--------------------------------------------------------------------------')
            posX, posY = input("Digite as coordenadas x e y separadas por espaço: ").split()
            posX = int(posX)
            posY = int(posY)
            
            if posX < 0 or posX > 3 or posY < 0 or posY > 3: #Se o usuário digitar alguma posição que não faça parte do tabuleiro, o programa pede para ele digitar novamente.
              print("Posição inválida! Fala outra ae.")
              time.sleep(1)
              os.system('cls') or None
              continue
            
            if posicoes_ocupadas[posX-1][posY-1] != 0: #Se o usuário digitar alguma posição que já foi ocupada, o programa pede para ele digitar novamente.
              print("Posição já ocupada, meu amigo! Fala outra ae.")
              time.sleep(1)
              os.system('cls') or None
              continue
            

            posicoes_ocupadas[posX-1][posY-1] = person1 #Se o jogador 1 digitou uma posição válida, o programa adiciona o número 1 nessa posição da matriz.
            x(currentMatch, posX-1, posY-1) #O jogador 1 é o "X". O programa chama a função de desenhar o "X" no tabuleiro nas coordenadas que o jogador 1 digitou.
            turn = person2  #Agora é a vez do jogador 2.
            count += 1  #Esse é o contador do empate. Se o contador for igual a 9, que é o número de posições da matriz, é porque os 2 jogadores preencheram todo o tabuleiro.
            time.sleep(1)
            os.system('cls') or None
            
        else:  #Mesma coisa das Linhas 53 a 70 porém para o jogador 2.
            print(f"VEZ DO JOGADOR: {j2} (O)")
            print('--------------------------------------------------------------------------')
            print('--------------------------------------------------------------------------')
            print("Canto superior esquerdo = (1, 1)" + '\n' + "Canto superior meio = (2, 1)" + '\n' + "Canto superior direito = (3, 1)")
            print("Canto meio esquerdo = (1, 2)" + '\n' + "Meio = (2, 2)" + '\n' + "Canto meio direito = (3, 2)")
            print("Canto inferior esquerdo = (1, 3)" + '\n' "Canto inferior meio = (2, 3)" + '\n' + "Canto inferior direito = (3, 3)")
            print('--------------------------------------------------------------------------')
            print('--------------------------------------------------------------------------')
            posX, posY = input("Digite as coordenadas x e y separadas por espaço: ").split()
            posX = int(posX)
            posY = int(posY)
            
            if posX < 0 or posX > 3 or posY < 0 or posY > 3:
                print("Posição inválida! Fala outra ae.")
                time.sleep(1)
                os.system('cls') or None
                continue
            
            
            if posicoes_ocupadas[posX-1][posY-1] != 0:
                print("Posição já ocupada, meu amigo! Fala outra ae.")
                time.sleep(1)
                os.system('cls') or None
                continue
            
            

            posicoes_ocupadas[posX-1][posY-1] = person2
            drawCircle(currentMatch, posX-1, posY-1)
            count += 1
            turn = person1
            time.sleep(1)
            os.system('cls') or None
            
        
        
        #Linhas (97 a 147) - Aqui são as condições de vitória e empate. O empate só acontece quando aquele contador que eu citei acima for igual a 9.
        #Existe vitória por linha, coluna e diagonal. Existem 8 possibilidades de vitória para cada jogador. Há 3 possibilidades de vitórias por linha, 
        # 3 por coluna e 2 por diagonais.
        
        if posicoes_ocupadas[0][0] == 1 and posicoes_ocupadas[1][0] == 1 and posicoes_ocupadas[2][0] == 1: 
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][1] == 1 and posicoes_ocupadas[1][1] == 1 and posicoes_ocupadas[2][1] == 1: 
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][2] == 1 and posicoes_ocupadas[1][2] == 1 and posicoes_ocupadas[2][2] == 1: 
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][0] == 1 and posicoes_ocupadas[1][1] == 1 and posicoes_ocupadas[2][2] == 1: 
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][0] == 1 and posicoes_ocupadas[0][1] == 1 and posicoes_ocupadas[0][2] == 1: 
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[1][0] == 1 and posicoes_ocupadas[1][1] == 1 and posicoes_ocupadas[1][2] == 1: 
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[2][0] == 1 and posicoes_ocupadas[2][1] == 1 and posicoes_ocupadas[2][2] == 1: 
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[2][0] == 1 and posicoes_ocupadas[1][1] == 1 and posicoes_ocupadas[0][2] == 1:
            print(f"{j1} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][0] == 2 and posicoes_ocupadas[1][0] == 1 and posicoes_ocupadas[2][0] == 2: 
            print(f"{j2} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][1] == 2 and posicoes_ocupadas[1][1] == 2 and posicoes_ocupadas[2][1] == 2: 
            print(f"{j2} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][2] == 2 and posicoes_ocupadas[1][2] == 2 and posicoes_ocupadas[2][2] == 2: 
            print(f"{j2} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][0] == 2 and posicoes_ocupadas[1][1] == 2 and posicoes_ocupadas[2][2] == 2: 
            print(f"{j2} Ganhou!!!")
            break
        elif posicoes_ocupadas[0][0] == 2 and posicoes_ocupadas[0][1] == 2 and posicoes_ocupadas[0][2] == 2: 
            print(f"{j2} Ganhou!!!")
            break
        elif posicoes_ocupadas[1][0] == 2 and posicoes_ocupadas[1][1] == 2 and posicoes_ocupadas[1][2] == 2: 
            print(f"{j2} Ganhou!!!")
            break
        elif posicoes_ocupadas[2][0] == 2 and posicoes_ocupadas[2][1] == 2 and posicoes_ocupadas[2][2] == 2: 
            print(f"{j2} Ganhou!!!")
            break
        elif posicoes_ocupadas[2][0] == 2 and posicoes_ocupadas[1][1] == 2 and posicoes_ocupadas[0][2] == 2:
            print(f"{j2} Ganhou!!!")
            break
        if count == 9:
            print("EMPATE!!")
            break        

        showimage(currentMatch)        

    print("Clique na janela do jogo e ressione a tecla 'q' para sair.")
    showimage_2(currentMatch)   #Mostra o tabuleiro do jogo finalizado.



if __name__ == '__main__':
    main()
    