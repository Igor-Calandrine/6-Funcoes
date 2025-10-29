"""Altere o programa da listagem 8.37 de forma que o usuário tenha três chances de acertar o número. O programa termina se o usuário acertar ou errar três vezes."""

import random

n = random.randint(1,10)

def jogo_adivinha(chances, numero):
    tentativas = []
    print(f"Você terá {chances} chances de acertar o número.")
    
    while True:
        x = int(input("Escolha um número entre 1 e 10: "))
        tentativas.append(x)

        if (x == numero):
            print("Você acertou!")
            break
        elif numero < x and chances >= 1:
            print("Errou! O número é menor")
            chances = chances - 1
            frase_tentativas(tentativas)
        elif numero > x and chances >= 1:
            print("Errou! O número é maior")
            chances = chances - 1
            frase_tentativas(tentativas)
        
        if chances >=1:
            print(f"Ainda resta mais {chances} chances")
        elif chances == 0:
            print(f"Número de tentativas encerradas.")
            print(f"O número era {n}")
            break

def frase_tentativas(lista):        
    frase = f"Números escolhidos ------> "
    for tentativa in lista:
        frase = frase + f" {tentativa}"
    print(frase)
    
jogo_adivinha(4, n)
