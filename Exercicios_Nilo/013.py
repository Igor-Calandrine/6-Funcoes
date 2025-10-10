"""Altere o programa da listagem 8.37 de forma que o usuário tenha três chances de acertar o número. O programa termina se o usuário acertar ou errar três vezes."""

import random

n = random.randint(1,10)

def jogo_adivinha(chances, numero):
    tentativas = []

    while chances > 0:
        x = int(input("Escolha um número entre 1 e 10: "))
        print(f"Você terá {chances} chances de acertar o número.")
        tentativas.append(x)

        if (x == numero):
            print("Você acertou!")
            break
        elif numero < x:
            print("O número é menor")
        elif numero > x and chances > 1:
            print("O número é maior")
        
        chances = chances - 1
        
        if chances > 1:
            print(f"Você errou, ainda resta mais {chances} chances")
        elif chances == 1:
            print(f"Você errou, ainda resta mais {chances} chance")
        else:
            print(f"Número de tentativas encerradas.")
            print(f"O número era {n}")
        
        frase = f"Números escolhidos - "
        for tentativa in tentativas:
            frase = frase + f" {tentativa}"
        print(frase)
        
jogo_adivinha(4, n)
