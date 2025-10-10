"""Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o tamanho da string estiver entre os valores de máximo e mínimo, e falso em caso contrário."""

def validar_str (min, max):
    palavra = ""
    palavra = input(f"Escreva uma palavra com no mínimo {min} e máximo {max} caracteres:\n\t")

    if len(palavra) < min or len(palavra) > max:
        print("Essa palavra é inválida.")
        print(f"Digite uma palavra com min ({min}) e max ({max}) caracteres.")
    else:
        print(f"Palavra válida - {len(palavra)} caracteres.")

validar_str(2, 6)
